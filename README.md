# Mica SDK for Python

Python client libraries for the [Mica](https://mica.io) network. Mica's API is [gRPC](https://grpc.io) over mutual TLS;
the messages and clients in this repository are generated from the
[public protos](https://github.com/1080network/proto).

## Which package do I need?

Each role is its own package, so you only install the code for the roles you play.

| Package | Use it if you are | Import |
| --- | --- | --- |
| `micaissuer` | an issuer | `mica.issuer...` |
| `micaacceptor` | an acceptor | `mica.acceptor...` |
| `micacommon` | everyone: shared messages and the mutual TLS helper. Installed automatically by the two above | `mica.common...`, `mica.member...`, `mica.sdk.mtls` |

```bash
pip install micaissuer      # or micaacceptor
```

Requires Python 3.10 or later, `protobuf` 6.32.1 or later (6 and 7 are both supported) and `grpcio` 1.74 or later.
Versions follow the proto release, in Python's version scheme: proto `v2.0.0` is `2.0.0`, and the pre-release
`v2.0.0-pre0` is `2.0.0rc0` (install it with `pip install --pre micaissuer`).

## Connecting

Mica uses mutual TLS. You need the root CA, and the client certificate and key Mica issued to you.

```python
from mica.sdk.mtls import MtlsCredentials, secure_channel
from mica.member.ping.v1 import ping_service_pb2, ping_service_pb2_grpc

credentials = MtlsCredentials.from_files("rootca.crt", "client.crt", "client.key")
with secure_channel("api.example.mica.io:443", credentials) as channel:
    response = ping_service_pb2_grpc.PingServiceStub(channel).Ping(ping_service_pb2.PingRequest())
    print(response.status)
```

Clients for each role are generated alongside their messages, for example
`mica.issuer.service.v2.issuer_to_mica_service_pb2_grpc.IssuerToMicaServiceStub`. Type stubs (`.pyi`) are included.

`examples/ping.py` is a complete program that connects and calls `Ping`, a good first check that your certificates and
network path work:

```bash
python examples/ping.py api.example.mica.io:443 rootca.crt client.crt client.key
```

## Repository layout

| Path | Contents |
| --- | --- |
| `common/`, `issuer/`, `acceptor/` | one distribution each; everything under `mica/` and `micashared/` is **generated**, except `common/mica/sdk` |
| `common/validate/` | `validate_pb2`, which the generated modules import and which isn't published elsewhere (generated) |
| `common/mica/sdk/mtls.py` | hand-written mutual TLS helper |
| `common/tests/` | tests, including a real mutual TLS call to an in-process server |
| `examples/` | runnable examples |
| `scripts/update-from-proto.sh` | regenerates the SDK for a proto release, builds the wheels and runs the tests |

The three distributions share the `mica` namespace (there is no `mica/__init__.py`), which is how `micaissuer` and
`micaacceptor` add `mica.issuer` and `mica.acceptor` to the `mica.common` that `micacommon` provides.

## Releasing (maintainers)

1. Run the **Generate SDKs** workflow in [1080network/proto](https://github.com/1080network/proto/actions) for the release tag.
2. Download its output: `gh run download <run-id> -R 1080network/proto -n generated-sdks-<version>`.
3. Run `scripts/update-from-proto.sh <version> <download-dir>`. It lays the generated code into the packages, sets the
   version, builds the wheels into `dist/`, and tests them in a clean environment, including against the oldest
   supported `protobuf` and `grpcio`.
4. Open a pull request with the changes and merge it.
5. Upload from the merged `main`, `micacommon` first: `twine upload dist/micacommon-*.whl` then the other two.
