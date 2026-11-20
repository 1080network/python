import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from mica.issuer.instrument.v2 import instrument_pb2 as _instrument_pb2
from micashared.common.v1 import address_pb2 as _address_pb2
from micashared.common.v1 import risk_signals_pb2 as _risk_signals_pb2
from micashared.common.v1 import transaction_pb2 as _transaction_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObtainValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ...) -> None: ...

class ObtainValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class ReverseObtainValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details", "original_transaction_identifier")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    original_transaction_identifier: OriginalTransactionIdentifier
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ...) -> None: ...

class ReverseObtainValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class RefundValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details", "original_transaction_identifier")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    original_transaction_identifier: OriginalTransactionIdentifier
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ...) -> None: ...

class RefundValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class PayoutValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ...) -> None: ...

class PayoutValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class HoldValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details", "expiration")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class HoldValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class ReleaseHoldValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details", "original_transaction_identifier")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    original_transaction_identifier: OriginalTransactionIdentifier
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ...) -> None: ...

class ReleaseHoldValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class ObtainHoldValueRequest(_message.Message):
    __slots__ = ("plan_name", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "risk_signal", "location_details", "original_transaction_identifier")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    risk_signal: _risk_signals_pb2.RiskSignal
    location_details: LocationDetails
    original_transaction_identifier: OriginalTransactionIdentifier
    def __init__(self, plan_name: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ...) -> None: ...

class ObtainHoldValueResponse(_message.Message):
    __slots__ = ("transaction_ref", "approved", "declined")
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    transaction_ref: str
    approved: ApprovedResult
    declined: DeclinedResult
    def __init__(self, transaction_ref: _Optional[str] = ..., approved: _Optional[_Union[ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[DeclinedResult, _Mapping]] = ...) -> None: ...

class IssuerFromMicaServicePingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IssuerFromMicaServicePingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocationDetails(_message.Message):
    __slots__ = ("organization_key", "organization_name", "organization_address", "category", "clerk_identifier")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLERK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_name: str
    organization_address: _address_pb2.Address
    category: str
    clerk_identifier: str
    def __init__(self, organization_key: _Optional[str] = ..., organization_name: _Optional[str] = ..., organization_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., category: _Optional[str] = ..., clerk_identifier: _Optional[str] = ...) -> None: ...

class OriginalTransactionIdentifier(_message.Message):
    __slots__ = ("transaction_identifier", "transaction_ref")
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    transaction_ref: str
    def __init__(self, transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., transaction_ref: _Optional[str] = ...) -> None: ...

class ApprovedResult(_message.Message):
    __slots__ = ("approved_amount",)
    APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    approved_amount: str
    def __init__(self, approved_amount: _Optional[str] = ...) -> None: ...

class DeclinedResult(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ValueAdviceRequest(_message.Message):
    __slots__ = ("value_advices",)
    VALUE_ADVICES_FIELD_NUMBER: _ClassVar[int]
    value_advices: _containers.RepeatedCompositeFieldContainer[ValueAdvice]
    def __init__(self, value_advices: _Optional[_Iterable[_Union[ValueAdvice, _Mapping]]] = ...) -> None: ...

class ValueAdviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValueAdvice(_message.Message):
    __slots__ = ("advice_priority", "advice_reason", "operation", "phase", "amount", "currency", "transaction_identifier", "issuer_instrument_key", "instrument_external_reference", "original_transaction_identifier", "transaction_ref")
    ADVICE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ADVICE_REASON_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    advice_priority: int
    advice_reason: str
    operation: str
    phase: str
    amount: str
    currency: _currency_pb2.Currency
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    issuer_instrument_key: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    original_transaction_identifier: OriginalTransactionIdentifier
    transaction_ref: str
    def __init__(self, advice_priority: _Optional[int] = ..., advice_reason: _Optional[str] = ..., operation: _Optional[str] = ..., phase: _Optional[str] = ..., amount: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ..., transaction_ref: _Optional[str] = ...) -> None: ...
