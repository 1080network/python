import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
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
    extraction: DataExtraction
    def __init__(self, status: _Optional[_Union[GetDataExtractionStatisticsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., extraction: _Optional[_Union[DataExtraction, _Mapping]] = ...) -> None: ...

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
    extractions: _containers.RepeatedCompositeFieldContainer[DataExtraction]
    def __init__(self, status: _Optional[_Union[SearchDataExtractionStatisticsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., extractions: _Optional[_Iterable[_Union[DataExtraction, _Mapping]]] = ...) -> None: ...
