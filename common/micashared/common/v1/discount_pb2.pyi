from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DiscountSummary(_message.Message):
    __slots__ = ("discount_amount", "discounts_applied")
    DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNTS_APPLIED_FIELD_NUMBER: _ClassVar[int]
    discount_amount: str
    discounts_applied: int
    def __init__(self, discount_amount: _Optional[str] = ..., discounts_applied: _Optional[int] = ...) -> None: ...
