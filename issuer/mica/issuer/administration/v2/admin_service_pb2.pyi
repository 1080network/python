import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.v1 import data_extraction_pb2 as _data_extraction_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import external_client_pb2 as _external_client_pb2
from micashared.common.v1 import mtls_certificate_pb2 as _mtls_certificate_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientAuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_AUTHENTICATION_TYPE_UNSPECIFIED: _ClassVar[ClientAuthenticationType]
    CLIENT_AUTHENTICATION_TYPE_CLIENT_CERTIFICATE: _ClassVar[ClientAuthenticationType]
    CLIENT_AUTHENTICATION_TYPE_API_TOKEN: _ClassVar[ClientAuthenticationType]
CLIENT_AUTHENTICATION_TYPE_UNSPECIFIED: ClientAuthenticationType
CLIENT_AUTHENTICATION_TYPE_CLIENT_CERTIFICATE: ClientAuthenticationType
CLIENT_AUTHENTICATION_TYPE_API_TOKEN: ClientAuthenticationType

class PingExternalRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingExternalResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingExternalWithCertificateRequest(_message.Message):
    __slots__ = ("certificate_id",)
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class PingExternalWithCertificateResponse(_message.Message):
    __slots__ = ("certificate_id",)
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class UpdateFromMicaClientCallbackAddressRequest(_message.Message):
    __slots__ = ("version", "callback_address")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    version: int
    callback_address: str
    def __init__(self, version: _Optional[int] = ..., callback_address: _Optional[str] = ...) -> None: ...

class UpdateFromMicaClientCallbackAddressResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateFromMicaClientCallbackAddressResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateFromMicaClientCallbackAddressResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateFromMicaClientCallbackAddressResponse.Status]
    STATUS_UNSPECIFIED: UpdateFromMicaClientCallbackAddressResponse.Status
    STATUS_SUCCESS: UpdateFromMicaClientCallbackAddressResponse.Status
    STATUS_ERROR: UpdateFromMicaClientCallbackAddressResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: UpdateFromMicaClientCallbackAddressResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[UpdateFromMicaClientCallbackAddressResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class GetFromMicaClientSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFromMicaClientSettingsResponse(_message.Message):
    __slots__ = ("status", "error", "settings")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetFromMicaClientSettingsResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetFromMicaClientSettingsResponse.Status]
        STATUS_ERROR: _ClassVar[GetFromMicaClientSettingsResponse.Status]
    STATUS_UNSPECIFIED: GetFromMicaClientSettingsResponse.Status
    STATUS_SUCCESS: GetFromMicaClientSettingsResponse.Status
    STATUS_ERROR: GetFromMicaClientSettingsResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    status: GetFromMicaClientSettingsResponse.Status
    error: _error_pb2.Error
    settings: _external_client_pb2.ExternalClientSettings
    def __init__(self, status: _Optional[_Union[GetFromMicaClientSettingsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., settings: _Optional[_Union[_external_client_pb2.ExternalClientSettings, _Mapping]] = ...) -> None: ...

class UpdateFromMicaClientAuthenticationTypeRequest(_message.Message):
    __slots__ = ("version", "authentication_type")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    version: int
    authentication_type: ClientAuthenticationType
    def __init__(self, version: _Optional[int] = ..., authentication_type: _Optional[_Union[ClientAuthenticationType, str]] = ...) -> None: ...

class UpdateFromMicaClientAuthenticationTypeResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateFromMicaClientAuthenticationTypeResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateFromMicaClientAuthenticationTypeResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateFromMicaClientAuthenticationTypeResponse.Status]
    STATUS_UNSPECIFIED: UpdateFromMicaClientAuthenticationTypeResponse.Status
    STATUS_SUCCESS: UpdateFromMicaClientAuthenticationTypeResponse.Status
    STATUS_ERROR: UpdateFromMicaClientAuthenticationTypeResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: UpdateFromMicaClientAuthenticationTypeResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[UpdateFromMicaClientAuthenticationTypeResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class ExternalClientSettings(_message.Message):
    __slots__ = ("version", "created", "updated", "callback_address", "client_authentication_settings")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_AUTHENTICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    callback_address: str
    client_authentication_settings: ClientAuthenticationSettings
    def __init__(self, version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., callback_address: _Optional[str] = ..., client_authentication_settings: _Optional[_Union[ClientAuthenticationSettings, _Mapping]] = ...) -> None: ...

class ClientAuthenticationSettings(_message.Message):
    __slots__ = ("suported_client_authentication_types", "current_authentication_type")
    SUPORTED_CLIENT_AUTHENTICATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    suported_client_authentication_types: _containers.RepeatedScalarFieldContainer[ClientAuthenticationType]
    current_authentication_type: ClientAuthenticationType
    def __init__(self, suported_client_authentication_types: _Optional[_Iterable[_Union[ClientAuthenticationType, str]]] = ..., current_authentication_type: _Optional[_Union[ClientAuthenticationType, str]] = ...) -> None: ...

class GenerateFromMicaClientCertificateRequest(_message.Message):
    __slots__ = ("display_name",)
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    def __init__(self, display_name: _Optional[str] = ...) -> None: ...

class GenerateFromMicaClientCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificate_to_sign")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GenerateFromMicaClientCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[GenerateFromMicaClientCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[GenerateFromMicaClientCertificateResponse.Status]
    STATUS_UNSPECIFIED: GenerateFromMicaClientCertificateResponse.Status
    STATUS_SUCCESS: GenerateFromMicaClientCertificateResponse.Status
    STATUS_ERROR: GenerateFromMicaClientCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TO_SIGN_FIELD_NUMBER: _ClassVar[int]
    status: GenerateFromMicaClientCertificateResponse.Status
    error: _error_pb2.Error
    certificate_to_sign: _mtls_certificate_pb2.FromMicaClientCertificate
    def __init__(self, status: _Optional[_Union[GenerateFromMicaClientCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificate_to_sign: _Optional[_Union[_mtls_certificate_pb2.FromMicaClientCertificate, _Mapping]] = ...) -> None: ...

class UpdateFromMicaClientCertificateRequest(_message.Message):
    __slots__ = ("certificate_id", "display_name", "base64_signed_cert_pem_from_csr", "base64_rootca_pem")
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE64_SIGNED_CERT_PEM_FROM_CSR_FIELD_NUMBER: _ClassVar[int]
    BASE64_ROOTCA_PEM_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    display_name: str
    base64_signed_cert_pem_from_csr: str
    base64_rootca_pem: str
    def __init__(self, certificate_id: _Optional[str] = ..., display_name: _Optional[str] = ..., base64_signed_cert_pem_from_csr: _Optional[str] = ..., base64_rootca_pem: _Optional[str] = ...) -> None: ...

class UpdateFromMicaClientCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificate")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateFromMicaClientCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateFromMicaClientCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateFromMicaClientCertificateResponse.Status]
    STATUS_UNSPECIFIED: UpdateFromMicaClientCertificateResponse.Status
    STATUS_SUCCESS: UpdateFromMicaClientCertificateResponse.Status
    STATUS_ERROR: UpdateFromMicaClientCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    status: UpdateFromMicaClientCertificateResponse.Status
    error: _error_pb2.Error
    certificate: _mtls_certificate_pb2.FromMicaClientCertificate
    def __init__(self, status: _Optional[_Union[UpdateFromMicaClientCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificate: _Optional[_Union[_mtls_certificate_pb2.FromMicaClientCertificate, _Mapping]] = ...) -> None: ...

class EnableFromMicaClientCertificateRequest(_message.Message):
    __slots__ = ("certificate_id",)
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class EnableFromMicaClientCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificate")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[EnableFromMicaClientCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[EnableFromMicaClientCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[EnableFromMicaClientCertificateResponse.Status]
    STATUS_UNSPECIFIED: EnableFromMicaClientCertificateResponse.Status
    STATUS_SUCCESS: EnableFromMicaClientCertificateResponse.Status
    STATUS_ERROR: EnableFromMicaClientCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    status: EnableFromMicaClientCertificateResponse.Status
    error: _error_pb2.Error
    certificate: _mtls_certificate_pb2.FromMicaClientCertificate
    def __init__(self, status: _Optional[_Union[EnableFromMicaClientCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificate: _Optional[_Union[_mtls_certificate_pb2.FromMicaClientCertificate, _Mapping]] = ...) -> None: ...

class SearchFromMicaClientCertificateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchFromMicaClientCertificateResponse(_message.Message):
    __slots__ = ("status", "error", "certificates")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchFromMicaClientCertificateResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchFromMicaClientCertificateResponse.Status]
        STATUS_ERROR: _ClassVar[SearchFromMicaClientCertificateResponse.Status]
    STATUS_UNSPECIFIED: SearchFromMicaClientCertificateResponse.Status
    STATUS_SUCCESS: SearchFromMicaClientCertificateResponse.Status
    STATUS_ERROR: SearchFromMicaClientCertificateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    status: SearchFromMicaClientCertificateResponse.Status
    error: _error_pb2.Error
    certificates: _containers.RepeatedCompositeFieldContainer[_mtls_certificate_pb2.FromMicaClientCertificate]
    def __init__(self, status: _Optional[_Union[SearchFromMicaClientCertificateResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., certificates: _Optional[_Iterable[_Union[_mtls_certificate_pb2.FromMicaClientCertificate, _Mapping]]] = ...) -> None: ...

class GetDataExtractionStatisticsRequest(_message.Message):
    __slots__ = ("extractor_name",)
    EXTRACTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    extractor_name: str
    def __init__(self, extractor_name: _Optional[str] = ...) -> None: ...

class GetDataExtractionStatisticsResponse(_message.Message):
    __slots__ = ("status", "error", "extraction")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetDataExtractionStatisticsResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetDataExtractionStatisticsResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetDataExtractionStatisticsResponse.Status]
        STATUS_ERROR: _ClassVar[GetDataExtractionStatisticsResponse.Status]
    STATUS_UNSPECIFIED: GetDataExtractionStatisticsResponse.Status
    STATUS_SUCCESS: GetDataExtractionStatisticsResponse.Status
    STATUS_NOT_FOUND: GetDataExtractionStatisticsResponse.Status
    STATUS_ERROR: GetDataExtractionStatisticsResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    status: GetDataExtractionStatisticsResponse.Status
    error: _error_pb2.Error
    extraction: _data_extraction_pb2.DataExtraction
    def __init__(self, status: _Optional[_Union[GetDataExtractionStatisticsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., extraction: _Optional[_Union[_data_extraction_pb2.DataExtraction, _Mapping]] = ...) -> None: ...

class SearchDataExtractionStatisticsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchDataExtractionStatisticsResponse(_message.Message):
    __slots__ = ("status", "error", "extractions")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchDataExtractionStatisticsResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchDataExtractionStatisticsResponse.Status]
        STATUS_ERROR: _ClassVar[SearchDataExtractionStatisticsResponse.Status]
    STATUS_UNSPECIFIED: SearchDataExtractionStatisticsResponse.Status
    STATUS_SUCCESS: SearchDataExtractionStatisticsResponse.Status
    STATUS_ERROR: SearchDataExtractionStatisticsResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXTRACTIONS_FIELD_NUMBER: _ClassVar[int]
    status: SearchDataExtractionStatisticsResponse.Status
    error: _error_pb2.Error
    extractions: _containers.RepeatedCompositeFieldContainer[_data_extraction_pb2.DataExtraction]
    def __init__(self, status: _Optional[_Union[SearchDataExtractionStatisticsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., extractions: _Optional[_Iterable[_Union[_data_extraction_pb2.DataExtraction, _Mapping]]] = ...) -> None: ...
