from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("street_lines", "locality", "region_code", "postal_code", "country_code")
    STREET_LINES_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    street_lines: _containers.RepeatedScalarFieldContainer[str]
    locality: str
    region_code: str
    postal_code: str
    country_code: str
    def __init__(self, street_lines: _Optional[_Iterable[str]] = ..., locality: _Optional[str] = ..., region_code: _Optional[str] = ..., postal_code: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...
