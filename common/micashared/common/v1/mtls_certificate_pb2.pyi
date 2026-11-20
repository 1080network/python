from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FromMicaClientCertificate(_message.Message):
    __slots__ = ("certificate_id", "display_name", "base64_certificate_pem", "base64_csr_pem", "base64_rootca_pem", "enabled", "use_host_trusted_certs")
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE64_CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    BASE64_CSR_PEM_FIELD_NUMBER: _ClassVar[int]
    BASE64_ROOTCA_PEM_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_HOST_TRUSTED_CERTS_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    display_name: str
    base64_certificate_pem: str
    base64_csr_pem: str
    base64_rootca_pem: str
    enabled: bool
    use_host_trusted_certs: bool
    def __init__(self, certificate_id: _Optional[str] = ..., display_name: _Optional[str] = ..., base64_certificate_pem: _Optional[str] = ..., base64_csr_pem: _Optional[str] = ..., base64_rootca_pem: _Optional[str] = ..., enabled: _Optional[bool] = ..., use_host_trusted_certs: _Optional[bool] = ...) -> None: ...
