from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MemberStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_STATUS_UNSPECIFIED: _ClassVar[MemberStatus]
    MEMBER_STATUS_ACTIVE: _ClassVar[MemberStatus]
    MEMBER_STATUS_INACTIVE: _ClassVar[MemberStatus]
MEMBER_STATUS_UNSPECIFIED: MemberStatus
MEMBER_STATUS_ACTIVE: MemberStatus
MEMBER_STATUS_INACTIVE: MemberStatus
