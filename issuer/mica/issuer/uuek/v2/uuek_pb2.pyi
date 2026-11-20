import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.issuer.instrument.v2 import instrument_pb2 as _instrument_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionIssuerUUEKRequest(_message.Message):
    __slots__ = ("issuer_instrument_key", "instrument_external_reference", "valid_from", "valid_to", "spend_limit", "number_of_uses", "unlimited")
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_TO_FIELD_NUMBER: _ClassVar[int]
    SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_USES_FIELD_NUMBER: _ClassVar[int]
    UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    valid_from: _timestamp_pb2.Timestamp
    valid_to: _timestamp_pb2.Timestamp
    spend_limit: str
    number_of_uses: int
    unlimited: bool
    def __init__(self, issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., valid_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., spend_limit: _Optional[str] = ..., number_of_uses: _Optional[int] = ..., unlimited: _Optional[bool] = ...) -> None: ...

class ProvisionIssuerUUEKResponse(_message.Message):
    __slots__ = ("status", "error", "issuer_uuek")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ProvisionIssuerUUEKResponse.Status]
        STATUS_SUCCESS: _ClassVar[ProvisionIssuerUUEKResponse.Status]
        STATUS_ERROR: _ClassVar[ProvisionIssuerUUEKResponse.Status]
        STATUS_INSTRUMENT_NOT_FOUND: _ClassVar[ProvisionIssuerUUEKResponse.Status]
        STATUS_INCORRECT_USE_CRITERIA: _ClassVar[ProvisionIssuerUUEKResponse.Status]
        STATUS_INVALID_ARGUMENT: _ClassVar[ProvisionIssuerUUEKResponse.Status]
    STATUS_UNSPECIFIED: ProvisionIssuerUUEKResponse.Status
    STATUS_SUCCESS: ProvisionIssuerUUEKResponse.Status
    STATUS_ERROR: ProvisionIssuerUUEKResponse.Status
    STATUS_INSTRUMENT_NOT_FOUND: ProvisionIssuerUUEKResponse.Status
    STATUS_INCORRECT_USE_CRITERIA: ProvisionIssuerUUEKResponse.Status
    STATUS_INVALID_ARGUMENT: ProvisionIssuerUUEKResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUER_UUEK_FIELD_NUMBER: _ClassVar[int]
    status: ProvisionIssuerUUEKResponse.Status
    error: _error_pb2.Error
    issuer_uuek: str
    def __init__(self, status: _Optional[_Union[ProvisionIssuerUUEKResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., issuer_uuek: _Optional[str] = ...) -> None: ...
