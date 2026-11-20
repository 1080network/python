from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Circle(_message.Message):
    __slots__ = ("latitude", "longitude", "radius")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    radius: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., radius: _Optional[int] = ...) -> None: ...
