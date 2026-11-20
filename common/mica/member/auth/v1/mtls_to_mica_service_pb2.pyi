import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MTLSCertificateSignatureRequest(_message.Message):
    __slots__ = ("base64_pem_csr",)
    BASE64_PEM_CSR_FIELD_NUMBER: _ClassVar[int]
    base64_pem_csr: str
    def __init__(self, base64_pem_csr: _Optional[str] = ...) -> None: ...

class ToMicaCertificate(_message.Message):
    __slots__ = ("serial_number", "issued", "expiry", "enabled", "base64_certificate_pem", "base64_rootca_pem", "roles", "display_name", "last_used")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ISSUED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASE64_CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    BASE64_ROOTCA_PEM_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    issued: _timestamp_pb2.Timestamp
    expiry: _timestamp_pb2.Timestamp
    enabled: bool
    base64_certificate_pem: str
    base64_rootca_pem: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    last_used: _timestamp_pb2.Timestamp
    def __init__(self, serial_number: _Optional[str] = ..., issued: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiry: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., enabled: _Optional[bool] = ..., base64_certificate_pem: _Optional[str] = ..., base64_rootca_pem: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., last_used: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateCertificateRequest(_message.Message):
    __slots__ = ("csr", "roles", "expire_in_duration", "display_name")
    CSR_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_IN_DURATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    csr: MTLSCertificateSignatureRequest
    roles: _containers.RepeatedScalarFieldContainer[str]
    expire_in_duration: str
    display_name: str
    def __init__(self, csr: _Optional[_Union[MTLSCertificateSignatureRequest, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ..., expire_in_duration: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class GenerateCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificate")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GenerateCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[GenerateCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[GenerateCertificateResponse.Status]
    STATUS_UNSPECIFIED: GenerateCertificateResponse.Status
    STATUS_SUCCESS: GenerateCertificateResponse.Status
    STATUS_ERROR: GenerateCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    status: GenerateCertificateResponse.Status
    error: _error_pb2.Error
    certificate: ToMicaCertificate
    def __init__(self, status: _Optional[_Union[GenerateCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificate: _Optional[_Union[ToMicaCertificate, _Mapping]] = ...) -> None: ...

class EnableCertificateRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class EnableCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "serial_number")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[EnableCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[EnableCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[EnableCertificateResponse.Status]
    STATUS_UNSPECIFIED: EnableCertificateResponse.Status
    STATUS_SUCCESS: EnableCertificateResponse.Status
    STATUS_ERROR: EnableCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    status: EnableCertificateResponse.Status
    error: _error_pb2.Error
    serial_number: str
    def __init__(self, status: _Optional[_Union[EnableCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., serial_number: _Optional[str] = ...) -> None: ...

class DisableCertificateRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class DisableCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "serial_number")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[DisableCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[DisableCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[DisableCertificateResponse.Status]
    STATUS_UNSPECIFIED: DisableCertificateResponse.Status
    STATUS_SUCCESS: DisableCertificateResponse.Status
    STATUS_ERROR: DisableCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    status: DisableCertificateResponse.Status
    error: _error_pb2.Error
    serial_number: str
    def __init__(self, status: _Optional[_Union[DisableCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., serial_number: _Optional[str] = ...) -> None: ...

class GetCertificateRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificate")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetCertificateResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[GetCertificateResponse.Status]
    STATUS_UNSPECIFIED: GetCertificateResponse.Status
    STATUS_SUCCESS: GetCertificateResponse.Status
    STATUS_NOT_FOUND: GetCertificateResponse.Status
    STATUS_ERROR: GetCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    status: GetCertificateResponse.Status
    error: _error_pb2.Error
    certificate: ToMicaCertificate
    def __init__(self, status: _Optional[_Union[GetCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificate: _Optional[_Union[ToMicaCertificate, _Mapping]] = ...) -> None: ...

class SearchCertificateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificates")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[SearchCertificateResponse.Status]
    STATUS_UNSPECIFIED: SearchCertificateResponse.Status
    STATUS_SUCCESS: SearchCertificateResponse.Status
    STATUS_ERROR: SearchCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    status: SearchCertificateResponse.Status
    error: _error_pb2.Error
    certificates: _containers.RepeatedCompositeFieldContainer[ToMicaCertificate]
    def __init__(self, status: _Optional[_Union[SearchCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificates: _Optional[_Iterable[_Union[ToMicaCertificate, _Mapping]]] = ...) -> None: ...
