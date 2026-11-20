import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionIdentifier(_message.Message):
    __slots__ = ("global_transaction_id", "global_transaction_time")
    GLOBAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TRANSACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    global_transaction_id: str
    global_transaction_time: _timestamp_pb2.Timestamp
    def __init__(self, global_transaction_id: _Optional[str] = ..., global_transaction_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
