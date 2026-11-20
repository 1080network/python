from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPROVAL_TYPE_UNSPECIFIED: _ClassVar[ApprovalType]
    APPROVAL_TYPE_FULL: _ClassVar[ApprovalType]
    APPROVAL_TYPE_PARTIAL: _ClassVar[ApprovalType]
APPROVAL_TYPE_UNSPECIFIED: ApprovalType
APPROVAL_TYPE_FULL: ApprovalType
APPROVAL_TYPE_PARTIAL: ApprovalType
