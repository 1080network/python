"""Open gRPC channels to the Mica network.

Every connection to Mica uses mutual TLS: the client presents a certificate issued by Mica and verifies Mica's
server certificate against the root certificate authority Mica provides.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence, Tuple, Union

import grpc

PathLike = Union[str, Path]


@dataclass(frozen=True)
class MtlsCredentials:
    """PEM-encoded material for a mutual TLS connection.

    Attributes:
        certificate_authorities: root certificate(s) used to verify Mica's server certificate.
        certificate: the client certificate chain issued by Mica.
        key: the private key for ``certificate``.
    """

    certificate_authorities: bytes
    certificate: bytes
    key: bytes

    @classmethod
    def from_files(cls, certificate_authorities: PathLike, certificate: PathLike, key: PathLike) -> "MtlsCredentials":
        """Read the credentials from PEM files on disk."""
        return cls(
            certificate_authorities=Path(certificate_authorities).read_bytes(),
            certificate=Path(certificate).read_bytes(),
            key=Path(key).read_bytes(),
        )

    def channel_credentials(self) -> grpc.ChannelCredentials:
        """Build the gRPC channel credentials."""
        return grpc.ssl_channel_credentials(
            root_certificates=self.certificate_authorities,
            private_key=self.key,
            certificate_chain=self.certificate,
        )


def secure_channel(
    target: str,
    credentials: MtlsCredentials,
    options: Optional[Sequence[Tuple[str, object]]] = None,
) -> grpc.Channel:
    """Open a mutual TLS channel to ``target`` (for example ``"api.example.mica.io:443"``).

    The caller owns the channel and should ``close()`` it when done (it is also a context manager).
    """
    return grpc.secure_channel(target, credentials.channel_credentials(), options=options)
