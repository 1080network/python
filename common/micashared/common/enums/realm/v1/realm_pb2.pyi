from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Realm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REALM_UNSPECIFIED: _ClassVar[Realm]
    REALM_ADMIN: _ClassVar[Realm]
    REALM_SERVICE: _ClassVar[Realm]
    REALM_USER: _ClassVar[Realm]
REALM_UNSPECIFIED: Realm
REALM_ADMIN: Realm
REALM_SERVICE: Realm
REALM_USER: Realm
