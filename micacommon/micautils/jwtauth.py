import collections

import grpc
import jwt

from datetime import datetime, timedelta, timezone
from typing import List, Dict


class _ClientCallDetails(
    collections.namedtuple(
        '_ClientCallDetails',
        ('method', 'timeout', 'metadata', 'credentials')),
    grpc.ClientCallDetails):
    pass


class MicaAuthNJWTInterceptor(grpc.UnaryUnaryClientInterceptor):

    def __init__(self, subject: str, audience: str, roles: List[str], jwt_key: str, extra_claims: Dict[str, str] = None):
        self.subject = subject
        self.audience = audience
        self.roles = roles
        self.jwt_key = jwt_key
        self.expiry = None
        self.authHeader = None
        self.extra_claims = extra_claims
        self.__generate_token()

    def intercept_unary_unary(self, continuation, client_call_details, request):
        duration = self.expiry - datetime.now(tz=timezone.utc)
        if duration.total_seconds() < 60:
            self.__generate_token()
        metadata = []

        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
            metadata.append(self.authHeader)
        else:
            metadata.append(self.authHeader)

        client_call_details = _ClientCallDetails(client_call_details.method, client_call_details.timeout, metadata,
                                                 client_call_details.credentials)
        return continuation(client_call_details, request)

    def __generate_token(self):
        self.expiry = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        claims = {"sub": self.subject, "aud": self.audience, "iss": "mica.io", "iat": datetime.now(tz=timezone.utc),
                  "exp": self.expiry, "roles": self.roles}
        for claim, value in self.extra_claims.items():
            claims[claim] = value
        encoded = jwt.encode(claims, self.jwt_key, algorithm="HS256")
        self.authHeader = ('authorization', f'Bearer {encoded}')
