import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataExtraction(_message.Message):
    __slots__ = ("extractor_name", "watermark_time", "last_execution_time", "records_processed")
    EXTRACTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    RECORDS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    extractor_name: str
    watermark_time: _timestamp_pb2.Timestamp
    last_execution_time: _timestamp_pb2.Timestamp
    records_processed: int
    def __init__(self, extractor_name: _Optional[str] = ..., watermark_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_execution_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., records_processed: _Optional[int] = ...) -> None: ...
