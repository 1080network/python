from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("message", "cid", "service_type", "full_method")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_METHOD_FIELD_NUMBER: _ClassVar[int]
    message: str
    cid: str
    service_type: str
    full_method: str
    def __init__(self, message: _Optional[str] = ..., cid: _Optional[str] = ..., service_type: _Optional[str] = ..., full_method: _Optional[str] = ...) -> None: ...
