import grpc
import base64

from sdk.mica.partner.service.v1.partner_to_mica_service_pb2_grpc import PartnerToMicaServiceStub
from sdk.mica.serviceprovider.service.v1.service_provider_to_mica_service_pb2_grpc import (
    ServiceProviderToMicaServiceStub
)


class CertLoader:
    root_certificates = None
    private_key = None
    certificate_chain = None

    def __init__(self, root_certificate_pem_file: str = None, root_certificate_b64: str = None, root_certificate_bytes: bytes = None,
                 private_key_pem_file: str = None, private_key_b64: str = None, private_key_bytes: bytes = None,
                 certificate_chain_pem_file: str = None, certificate_chain_b64: str = None, certificate_chain_bytes: bytes = None
                 ):
        if root_certificate_pem_file is not None:
            self.root_certificates = bytes(open(root_certificate_pem_file, 'rb').read())
        elif root_certificate_b64 is not None:
            self.root_certificates = base64.b64decode(root_certificate_b64)
        elif root_certificate_bytes is not None:
            self.root_certificates = root_certificate_bytes
        else:
            raise ValueError('no root certificate set')

        if private_key_pem_file is not None:
            self.private_key = bytes(open(private_key_pem_file, "rb").read())
        elif private_key_b64 is not None:
            self.private_key = base64.b64decode(private_key_b64)
        elif private_key_bytes is not None:
            self.private_key = private_key_bytes
        else:
            raise ValueError('no private key set')

        if certificate_chain_pem_file is not None:
            self.certificate_chain = bytes(open(certificate_chain_pem_file, "rb").read())
        elif certificate_chain_b64 is not None:
            self.certificate_chain = base64.b64decode(certificate_chain_b64)
        elif certificate_chain_bytes is not None:
            self.certificate_chain = certificate_chain_bytes
        else:
            raise ValueError('no certificate chain set')

    def to_ssl_credentials(self):
        return grpc.ssl_channel_credentials(root_certificates=self.root_certificates,
                                            private_key=self.private_key,
                                            certificate_chain=self.certificate_chain)


def create_channel(addr: str, credentials: grpc.ChannelCredentials = None, options=None, compression=None):
    return grpc.secure_channel(target=addr,
                               credentials=credentials,
                               options=options,
                               compression=compression
                               )


def build_partner_client(channel: grpc.Channel):
    # builds the client stub for a partner
    stub = PartnerToMicaServiceStub(channel=channel)
    return stub


def build_service_provider_client(channel: grpc.Channel):
    # builds the client stub for a service provider
    stub = ServiceProviderToMicaServiceStub(channel=channel)
    return stub
