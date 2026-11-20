from validate import validate_pb2 as _validate_pb2
from micashared.common.enums.lineitemstatus.v1 import line_item_status_pb2 as _line_item_status_pb2
from micashared.common.enums.unit.v1 import unit_pb2 as _unit_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdjustmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADJUSTMENT_TYPE_UNSPECIFIED: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_MANUFACTURER_DISCOUNT: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_STORE_DISCOUNT: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_RETURN: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_PAYMENT_CASH: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_PAYMENT_GIFT_CARD: _ClassVar[AdjustmentType]
    ADJUSTMENT_TYPE_PAYMENT_OTHER: _ClassVar[AdjustmentType]
ADJUSTMENT_TYPE_UNSPECIFIED: AdjustmentType
ADJUSTMENT_TYPE_MANUFACTURER_DISCOUNT: AdjustmentType
ADJUSTMENT_TYPE_STORE_DISCOUNT: AdjustmentType
ADJUSTMENT_TYPE_RETURN: AdjustmentType
ADJUSTMENT_TYPE_PAYMENT_CASH: AdjustmentType
ADJUSTMENT_TYPE_PAYMENT_GIFT_CARD: AdjustmentType
ADJUSTMENT_TYPE_PAYMENT_OTHER: AdjustmentType

class LineItem(_message.Message):
    __slots__ = ("sequence", "line_item_group", "product_code", "description", "quantity", "unit", "unit_amount", "unit_tax_amount", "line_amount", "line_tax_amount")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEM_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LINE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LINE_TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    line_item_group: str
    product_code: str
    description: str
    quantity: str
    unit: _unit_pb2.Unit
    unit_amount: str
    unit_tax_amount: str
    line_amount: str
    line_tax_amount: str
    def __init__(self, sequence: _Optional[int] = ..., line_item_group: _Optional[str] = ..., product_code: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[str] = ..., unit: _Optional[_Union[_unit_pb2.Unit, str]] = ..., unit_amount: _Optional[str] = ..., unit_tax_amount: _Optional[str] = ..., line_amount: _Optional[str] = ..., line_tax_amount: _Optional[str] = ...) -> None: ...

class LineItemWrapper(_message.Message):
    __slots__ = ("line_items",)
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    line_items: _containers.RepeatedCompositeFieldContainer[LineItem]
    def __init__(self, line_items: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ...) -> None: ...

class Adjustment(_message.Message):
    __slots__ = ("sequence", "adjustment_type", "product_code", "description", "quantity", "unit", "unit_amount", "unit_tax_amount", "line_amount", "line_tax_amount")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LINE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LINE_TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    adjustment_type: AdjustmentType
    product_code: str
    description: str
    quantity: str
    unit: _unit_pb2.Unit
    unit_amount: str
    unit_tax_amount: str
    line_amount: str
    line_tax_amount: str
    def __init__(self, sequence: _Optional[int] = ..., adjustment_type: _Optional[_Union[AdjustmentType, str]] = ..., product_code: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[str] = ..., unit: _Optional[_Union[_unit_pb2.Unit, str]] = ..., unit_amount: _Optional[str] = ..., unit_tax_amount: _Optional[str] = ..., line_amount: _Optional[str] = ..., line_tax_amount: _Optional[str] = ...) -> None: ...

class LineItemSequenceAndStatus(_message.Message):
    __slots__ = ("sequence", "status")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    status: _line_item_status_pb2.LineItemStatus
    def __init__(self, sequence: _Optional[int] = ..., status: _Optional[_Union[_line_item_status_pb2.LineItemStatus, str]] = ...) -> None: ...

class LineItemSequenceAndStatusValue(_message.Message):
    __slots__ = ("line_item_sequence_and_statuses",)
    LINE_ITEM_SEQUENCE_AND_STATUSES_FIELD_NUMBER: _ClassVar[int]
    line_item_sequence_and_statuses: _containers.RepeatedCompositeFieldContainer[LineItemSequenceAndStatus]
    def __init__(self, line_item_sequence_and_statuses: _Optional[_Iterable[_Union[LineItemSequenceAndStatus, _Mapping]]] = ...) -> None: ...

class LineItemAndStatus(_message.Message):
    __slots__ = ("line_item", "status")
    LINE_ITEM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    line_item: LineItem
    status: _line_item_status_pb2.LineItemStatus
    def __init__(self, line_item: _Optional[_Union[LineItem, _Mapping]] = ..., status: _Optional[_Union[_line_item_status_pb2.LineItemStatus, str]] = ...) -> None: ...

class LineItemResponseValue(_message.Message):
    __slots__ = ("line_item_and_statuses",)
    LINE_ITEM_AND_STATUSES_FIELD_NUMBER: _ClassVar[int]
    line_item_and_statuses: _containers.RepeatedCompositeFieldContainer[LineItemAndStatus]
    def __init__(self, line_item_and_statuses: _Optional[_Iterable[_Union[LineItemAndStatus, _Mapping]]] = ...) -> None: ...

class Surcharge(_message.Message):
    __slots__ = ("description", "amount")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    description: str
    amount: str
    def __init__(self, description: _Optional[str] = ..., amount: _Optional[str] = ...) -> None: ...
