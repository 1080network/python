from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BarcodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BARCODE_TYPE_UNSPECIFIED: _ClassVar[BarcodeType]
    BARCODE_TYPE_NONE: _ClassVar[BarcodeType]
    BARCODE_TYPE_QR: _ClassVar[BarcodeType]
    BARCODE_TYPE_EAN128: _ClassVar[BarcodeType]
BARCODE_TYPE_UNSPECIFIED: BarcodeType
BARCODE_TYPE_NONE: BarcodeType
BARCODE_TYPE_QR: BarcodeType
BARCODE_TYPE_EAN128: BarcodeType
