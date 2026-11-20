import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
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
