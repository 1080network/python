import base64
from datetime import datetime, timedelta, timezone

import grpc
from typing import List

import jwt

from micautils.jwtauth import MicaAuthNJWTInterceptor

base64_default_jwt_key = 'idv7Nf/7476PxbMX6iVIXHCc/kMSqSjPQNgBNDU2kz4='


class CertLoader:
    root_certificates = None
    private_key = None
    certificate_chain = None

    def __init__(self, root_certificate_pem_file: str = None, root_certificate_bytes: bytes = None,
                 private_key_pem_file: str = None, private_key_bytes: bytes = None):
        if root_certificate_pem_file is not None:
            self.root_certificates = open(root_certificate_pem_file, 'rb').read()
        else:
            self.root_certificates = root_certificate_bytes
        if private_key_pem_file is not None:
            self.private_key


def create_channel(addr: str, credentials: grpc.ChannelCredentials = None, certificates: CertLoader = None,
                   base64_jwt_key: str = base64_default_jwt_key, jwt_roles: List[str] = None,
                   options=None, compression=None):
    if certificates is None and credentials is None:
        insecure = grpc.insecure_channel(addr, options, compression)
        jwt_key = base64.b64decode(base64_jwt_key)
        jwt_interceptor = MicaAuthNJWTInterceptor(roles=jwt_roles, jwt_key=jwt_key)
        return grpc.intercept_channel(insecure, jwt_interceptor)
    else:
        if credentials is None:
            credentials = grpc.ssl_channel_credentials(root_certificates=certificates.root_certificates,
                                                       private_key=certificates.private_key,
                                                       certificate_chain=certificates.certificate_chain)
        return grpc.secure_channel(target=addr,
                                   credentials=credentials,
                                   options=options,
                                   compression=compression
                                   )


def create_test_jwt_token(jwt_roles: List[str], base64_jwt_key: str = base64_default_jwt_key):
    expiry = datetime.now(tz=timezone.utc) + timedelta(hours=1)
    claims = {"iss": "mica.io", "iat": datetime.now(tz=timezone.utc), "exp": expiry, "roles": jwt_roles}
    jwt_key = base64.b64decode(base64_jwt_key)
    encoded = jwt.encode(claims, jwt_key, algorithm="HS256")
    return encoded
