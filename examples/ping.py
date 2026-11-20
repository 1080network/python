"""Connect to Mica with mutual TLS and call Ping, a good first check that your certificates and network path work.

    python examples/ping.py api.example.mica.io:443 rootca.crt client.crt client.key
"""

import sys

from mica.member.ping.v1 import ping_service_pb2, ping_service_pb2_grpc
from mica.sdk.mtls import MtlsCredentials, secure_channel


def main() -> None:
    if len(sys.argv) != 5:
        sys.exit("usage: ping.py <host:port> <rootca.crt> <client.crt> <client.key>")
    target, ca, cert, key = sys.argv[1:]
    credentials = MtlsCredentials.from_files(ca, cert, key)
    with secure_channel(target, credentials) as channel:
        response = ping_service_pb2_grpc.PingServiceStub(channel).Ping(ping_service_pb2.PingRequest(), timeout=15)
    print(f"status={ping_service_pb2.PingResponse.Status.Name(response.status)} "
          f"service={response.service_type} version={response.build_version}")


if __name__ == "__main__":
    main()
