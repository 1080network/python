from mica.common.v1 import currency_pb2 as _currency_pb2
from mica.issuer.instrument.v2 import instrument_pb2 as _instrument_pb2
from mica.issuer.value.v2 import value_pb2 as _value_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import transaction_pb2 as _transaction_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveChargebackRequest(_message.Message):
    __slots__ = ("issuer_instrument_key", "instrument_external_reference", "currency", "requested_amount", "original_transaction_identifier")
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    currency: _currency_pb2.Currency
    requested_amount: str
    original_transaction_identifier: _transaction_pb2.TransactionIdentifier
    def __init__(self, issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., requested_amount: _Optional[str] = ..., original_transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ...) -> None: ...

class ApproveChargebackResponse(_message.Message):
    __slots__ = ("status", "error", "approval_operation_ref", "message")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ApproveChargebackResponse.Status]
        STATUS_FULL_APPROVAL: _ClassVar[ApproveChargebackResponse.Status]
        STATUS_NOT_APPROVED: _ClassVar[ApproveChargebackResponse.Status]
        STATUS_ERROR: _ClassVar[ApproveChargebackResponse.Status]
    STATUS_UNSPECIFIED: ApproveChargebackResponse.Status
    STATUS_FULL_APPROVAL: ApproveChargebackResponse.Status
    STATUS_NOT_APPROVED: ApproveChargebackResponse.Status
    STATUS_ERROR: ApproveChargebackResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_OPERATION_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: ApproveChargebackResponse.Status
    error: _error_pb2.Error
    approval_operation_ref: str
    message: str
    def __init__(self, status: _Optional[_Union[ApproveChargebackResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., approval_operation_ref: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
