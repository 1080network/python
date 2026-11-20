from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Pagination(_message.Message):
    __slots__ = ("page_size", "page_number", "total_count")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_number: int
    total_count: int
    def __init__(self, page_size: _Optional[int] = ..., page_number: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...
