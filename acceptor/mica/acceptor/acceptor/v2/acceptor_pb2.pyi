import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.v1 import address_pb2 as _address_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Acceptor(_message.Message):
    __slots__ = ("acceptor_key", "version", "created", "updated", "name", "tax_identifier", "address", "callback_address", "network_group", "features")
    ACCEPTOR_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAX_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_GROUP_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    acceptor_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    name: str
    tax_identifier: str
    address: _address_pb2.Address
    callback_address: str
    network_group: str
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, acceptor_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., tax_identifier: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., callback_address: _Optional[str] = ..., network_group: _Optional[str] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAcceptorRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAcceptorResponse(_message.Message):
    __slots__ = ("status", "error", "acceptor")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetAcceptorResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetAcceptorResponse.Status]
        STATUS_ERROR: _ClassVar[GetAcceptorResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetAcceptorResponse.Status]
    STATUS_UNSPECIFIED: GetAcceptorResponse.Status
    STATUS_SUCCESS: GetAcceptorResponse.Status
    STATUS_ERROR: GetAcceptorResponse.Status
    STATUS_NOT_FOUND: GetAcceptorResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FIELD_NUMBER: _ClassVar[int]
    status: GetAcceptorResponse.Status
    error: _error_pb2.Error
    acceptor: Acceptor
    def __init__(self, status: _Optional[_Union[GetAcceptorResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., acceptor: _Optional[_Union[Acceptor, _Mapping]] = ...) -> None: ...
