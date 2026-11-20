from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_OPERATION_TYPE_UNSPECIFIED: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_OBTAIN: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_RETURN: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_REVERSE_OBTAIN: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_REVERSE_RETURN: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_P2P: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_HOLD: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_RELEASE: _ClassVar[ValueOperationType]
    VALUE_OPERATION_TYPE_OBTAIN_HOLD: _ClassVar[ValueOperationType]
VALUE_OPERATION_TYPE_UNSPECIFIED: ValueOperationType
VALUE_OPERATION_TYPE_OBTAIN: ValueOperationType
VALUE_OPERATION_TYPE_RETURN: ValueOperationType
VALUE_OPERATION_TYPE_REVERSE_OBTAIN: ValueOperationType
VALUE_OPERATION_TYPE_REVERSE_RETURN: ValueOperationType
VALUE_OPERATION_TYPE_P2P: ValueOperationType
VALUE_OPERATION_TYPE_HOLD: ValueOperationType
VALUE_OPERATION_TYPE_RELEASE: ValueOperationType
VALUE_OPERATION_TYPE_OBTAIN_HOLD: ValueOperationType
