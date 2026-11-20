import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("status", "server_time", "server_start_time", "build_version", "build_sha", "build_time", "service_type")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[PingResponse.Status]
        STATUS_SUCCESS: _ClassVar[PingResponse.Status]
    STATUS_UNSPECIFIED: PingResponse.Status
    STATUS_SUCCESS: PingResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_START_TIME_FIELD_NUMBER: _ClassVar[int]
    BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_SHA_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    status: PingResponse.Status
    server_time: _timestamp_pb2.Timestamp
    server_start_time: _timestamp_pb2.Timestamp
    build_version: str
    build_sha: str
    build_time: str
    service_type: str
    def __init__(self, status: _Optional[_Union[PingResponse.Status, str]] = ..., server_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., server_start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., build_version: _Optional[str] = ..., build_sha: _Optional[str] = ..., build_time: _Optional[str] = ..., service_type: _Optional[str] = ...) -> None: ...
