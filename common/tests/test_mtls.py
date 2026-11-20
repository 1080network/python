"""Makes real mutual TLS Ping calls to an in-process server, using certificates generated for the test."""

import datetime
import ipaddress
from concurrent import futures

import grpc
import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import NameOID

from mica.member.ping.v1 import ping_service_pb2, ping_service_pb2_grpc
from mica.sdk.mtls import MtlsCredentials, secure_channel


class _Identity:
    def __init__(self, name, ca=None):
        self.key = ec.generate_private_key(ec.SECP256R1())
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, name)])
        issuer_name = ca.cert.subject if ca else subject
        signing_key = ca.key if ca else self.key
        now = datetime.datetime.now(datetime.timezone.utc)
        builder = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer_name)
            .public_key(self.key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - datetime.timedelta(minutes=1))
            .not_valid_after(now + datetime.timedelta(hours=1))
            .add_extension(x509.BasicConstraints(ca=ca is None, path_length=None), critical=True)
            .add_extension(
                x509.SubjectAlternativeName(
                    [x509.IPAddress(ipaddress.ip_address("127.0.0.1")), x509.DNSName("localhost")]
                ),
                critical=False,
            )
        )
        self.cert = builder.sign(signing_key, hashes.SHA256())

    @property
    def cert_pem(self):
        return self.cert.public_bytes(serialization.Encoding.PEM)

    @property
    def key_pem(self):
        return self.key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()
        )


class _PingServicer(ping_service_pb2_grpc.PingServiceServicer):
    def Ping(self, request, context):
        return ping_service_pb2.PingResponse(status=ping_service_pb2.PingResponse.STATUS_SUCCESS, service_type="test")


@pytest.fixture
def server_and_ca():
    ca = _Identity("test ca")
    server_identity = _Identity("server", ca)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    ping_service_pb2_grpc.add_PingServiceServicer_to_server(_PingServicer(), server)
    server_credentials = grpc.ssl_server_credentials(
        [(server_identity.key_pem, server_identity.cert_pem)],
        root_certificates=ca.cert_pem,
        require_client_auth=True,
    )
    port = server.add_secure_port("127.0.0.1:0", server_credentials)
    server.start()
    yield f"127.0.0.1:{port}", ca
    server.stop(0)


def test_ping_over_mutual_tls(server_and_ca):
    target, ca = server_and_ca
    client = _Identity("client", ca)
    credentials = MtlsCredentials(ca.cert_pem, client.cert_pem, client.key_pem)
    with secure_channel(target, credentials) as channel:
        response = ping_service_pb2_grpc.PingServiceStub(channel).Ping(ping_service_pb2.PingRequest(), timeout=10)
    assert response.status == ping_service_pb2.PingResponse.STATUS_SUCCESS


def test_server_from_unknown_authority_is_rejected(server_and_ca):
    target, ca = server_and_ca
    client = _Identity("client", ca)
    other_ca = _Identity("other ca")
    credentials = MtlsCredentials(other_ca.cert_pem, client.cert_pem, client.key_pem)
    with secure_channel(target, credentials) as channel:
        with pytest.raises(grpc.RpcError):
            ping_service_pb2_grpc.PingServiceStub(channel).Ping(ping_service_pb2.PingRequest(), timeout=10)
