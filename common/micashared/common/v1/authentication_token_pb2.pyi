from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationHeaderConfiguration(_message.Message):
    __slots__ = ("header_key", "header_value_prefix")
    HEADER_KEY_FIELD_NUMBER: _ClassVar[int]
    HEADER_VALUE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    header_key: str
    header_value_prefix: str
    def __init__(self, header_key: _Optional[str] = ..., header_value_prefix: _Optional[str] = ...) -> None: ...

class ApiTokenConfiguration(_message.Message):
    __slots__ = ("header_configuration", "api_token_value", "pem_ca_chain")
    HEADER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    API_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    PEM_CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    header_configuration: AuthenticationHeaderConfiguration
    api_token_value: str
    pem_ca_chain: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header_configuration: _Optional[_Union[AuthenticationHeaderConfiguration, _Mapping]] = ..., api_token_value: _Optional[str] = ..., pem_ca_chain: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateApiTokenConfigurationRequest(_message.Message):
    __slots__ = ("header_configuration", "api_token_value", "pem_ca_chain")
    HEADER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    API_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    PEM_CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    header_configuration: AuthenticationHeaderConfiguration
    api_token_value: str
    pem_ca_chain: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header_configuration: _Optional[_Union[AuthenticationHeaderConfiguration, _Mapping]] = ..., api_token_value: _Optional[str] = ..., pem_ca_chain: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateApiTokenConfigurationResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[CreateApiTokenConfigurationResponse.Status]
        STATUS_SUCCESS: _ClassVar[CreateApiTokenConfigurationResponse.Status]
        STATUS_ERROR: _ClassVar[CreateApiTokenConfigurationResponse.Status]
    STATUS_UNSPECIFIED: CreateApiTokenConfigurationResponse.Status
    STATUS_SUCCESS: CreateApiTokenConfigurationResponse.Status
    STATUS_ERROR: CreateApiTokenConfigurationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: CreateApiTokenConfigurationResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[CreateApiTokenConfigurationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class GetApiTokenConfigurationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetApiTokenConfigurationResponse(_message.Message):
    __slots__ = ("status", "error", "api_token_configuration")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetApiTokenConfigurationResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetApiTokenConfigurationResponse.Status]
        STATUS_ERROR: _ClassVar[GetApiTokenConfigurationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetApiTokenConfigurationResponse.Status]
    STATUS_UNSPECIFIED: GetApiTokenConfigurationResponse.Status
    STATUS_SUCCESS: GetApiTokenConfigurationResponse.Status
    STATUS_ERROR: GetApiTokenConfigurationResponse.Status
    STATUS_NOT_FOUND: GetApiTokenConfigurationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    API_TOKEN_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    status: GetApiTokenConfigurationResponse.Status
    error: _error_pb2.Error
    api_token_configuration: ApiTokenConfiguration
    def __init__(self, status: _Optional[_Union[GetApiTokenConfigurationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., api_token_configuration: _Optional[_Union[ApiTokenConfiguration, _Mapping]] = ...) -> None: ...

class UpdateApiTokenConfigurationRequest(_message.Message):
    __slots__ = ("header_configuration", "api_token_value", "pem_ca_chain")
    HEADER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    API_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    PEM_CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    header_configuration: AuthenticationHeaderConfiguration
    api_token_value: str
    pem_ca_chain: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header_configuration: _Optional[_Union[AuthenticationHeaderConfiguration, _Mapping]] = ..., api_token_value: _Optional[str] = ..., pem_ca_chain: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateApiTokenConfigurationResponse(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateApiTokenConfigurationResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateApiTokenConfigurationResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateApiTokenConfigurationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[UpdateApiTokenConfigurationResponse.Status]
    STATUS_UNSPECIFIED: UpdateApiTokenConfigurationResponse.Status
    STATUS_SUCCESS: UpdateApiTokenConfigurationResponse.Status
    STATUS_ERROR: UpdateApiTokenConfigurationResponse.Status
    STATUS_NOT_FOUND: UpdateApiTokenConfigurationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: UpdateApiTokenConfigurationResponse.Status
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[UpdateApiTokenConfigurationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
