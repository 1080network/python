from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BarcodeLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BARCODE_LOCATION_UNSPECIFIED: _ClassVar[BarcodeLocation]
    BARCODE_LOCATION_NONE: _ClassVar[BarcodeLocation]
    BARCODE_LOCATION_TOP: _ClassVar[BarcodeLocation]
    BARCODE_LOCATION_BOTTOM: _ClassVar[BarcodeLocation]
BARCODE_LOCATION_UNSPECIFIED: BarcodeLocation
BARCODE_LOCATION_NONE: BarcodeLocation
BARCODE_LOCATION_TOP: BarcodeLocation
BARCODE_LOCATION_BOTTOM: BarcodeLocation
