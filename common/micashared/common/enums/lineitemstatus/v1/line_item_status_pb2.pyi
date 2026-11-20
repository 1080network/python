from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LineItemStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_ITEM_STATUS_UNSPECIFIED: _ClassVar[LineItemStatus]
    LINE_ITEM_STATUS_NOT_ASSESSED: _ClassVar[LineItemStatus]
    LINE_ITEM_STATUS_ELIGIBLE: _ClassVar[LineItemStatus]
    LINE_ITEM_STATUS_INELIGIBLE: _ClassVar[LineItemStatus]
    LINE_ITEM_STATUS_AGE_RESTRICTED: _ClassVar[LineItemStatus]
LINE_ITEM_STATUS_UNSPECIFIED: LineItemStatus
LINE_ITEM_STATUS_NOT_ASSESSED: LineItemStatus
LINE_ITEM_STATUS_ELIGIBLE: LineItemStatus
LINE_ITEM_STATUS_INELIGIBLE: LineItemStatus
LINE_ITEM_STATUS_AGE_RESTRICTED: LineItemStatus
