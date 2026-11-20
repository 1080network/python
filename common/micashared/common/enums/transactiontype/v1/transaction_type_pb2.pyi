from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_TYPE_UNSPECIFIED: _ClassVar[TransactionType]
    TRANSACTION_TYPE_OBTAIN: _ClassVar[TransactionType]
    TRANSACTION_TYPE_RETURN: _ClassVar[TransactionType]
    TRANSACTION_TYPE_P2P: _ClassVar[TransactionType]
TRANSACTION_TYPE_UNSPECIFIED: TransactionType
TRANSACTION_TYPE_OBTAIN: TransactionType
TRANSACTION_TYPE_RETURN: TransactionType
TRANSACTION_TYPE_P2P: TransactionType
