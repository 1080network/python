import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from mica.issuer.instrument.v2 import instrument_pb2 as _instrument_pb2
from micashared.common.enums.valueoperationtype.v1 import value_operation_type_pb2 as _value_operation_type_pb2
from micashared.common.v1 import address_pb2 as _address_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import risk_signals_pb2 as _risk_signals_pb2
from micashared.common.v1 import transaction_pb2 as _transaction_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PINStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIN_STATUS_UNSPECIFIED: _ClassVar[PINStatus]
    PIN_STATUS_MATCH: _ClassVar[PINStatus]
PIN_STATUS_UNSPECIFIED: PINStatus
PIN_STATUS_MATCH: PINStatus

class Value(_message.Message):
    __slots__ = ("transaction_key", "version", "created", "updated", "operation_type", "issuer_instrument_key", "issuer_instrument_ref", "issuer_uuek", "acceptor_transaction_ref", "organization_key", "organization_name", "organization_address", "category", "clerk_identifier", "total_amount", "discount_amount", "ineligible_amount", "requested_amount", "order_number", "expiration", "initial_acceptor_transaction_ref", "currency")
    TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_UUEK_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLERK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INELIGIBLE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ACCEPTOR_TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transaction_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    operation_type: _value_operation_type_pb2.ValueOperationType
    issuer_instrument_key: str
    issuer_instrument_ref: str
    issuer_uuek: str
    acceptor_transaction_ref: str
    organization_key: str
    organization_name: str
    organization_address: _address_pb2.Address
    category: str
    clerk_identifier: str
    total_amount: str
    discount_amount: str
    ineligible_amount: str
    requested_amount: str
    order_number: str
    expiration: _timestamp_pb2.Timestamp
    initial_acceptor_transaction_ref: str
    currency: _currency_pb2.Currency
    def __init__(self, transaction_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., operation_type: _Optional[_Union[_value_operation_type_pb2.ValueOperationType, str]] = ..., issuer_instrument_key: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ..., issuer_uuek: _Optional[str] = ..., acceptor_transaction_ref: _Optional[str] = ..., organization_key: _Optional[str] = ..., organization_name: _Optional[str] = ..., organization_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., category: _Optional[str] = ..., clerk_identifier: _Optional[str] = ..., total_amount: _Optional[str] = ..., discount_amount: _Optional[str] = ..., ineligible_amount: _Optional[str] = ..., requested_amount: _Optional[str] = ..., order_number: _Optional[str] = ..., expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., initial_acceptor_transaction_ref: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ...) -> None: ...

class From(_message.Message):
    __slots__ = ("uuek", "first_name", "last_name", "email", "issuer_name")
    UUEK_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ISSUER_NAME_FIELD_NUMBER: _ClassVar[int]
    uuek: str
    first_name: str
    last_name: str
    email: str
    issuer_name: str
    def __init__(self, uuek: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., issuer_name: _Optional[str] = ...) -> None: ...

class ReceiveValueRequest(_message.Message):
    __slots__ = ("to_issuer_instrument_key", "to_issuer_instrument_ref", "instrument_external_reference", "currency", "amount", "risk_signal", "transaction_identifier")
    TO_ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    TO_ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    to_issuer_instrument_key: str
    to_issuer_instrument_ref: str
    instrument_external_reference: _instrument_pb2.InstrumentExternalReference
    currency: _currency_pb2.Currency
    amount: str
    risk_signal: _risk_signals_pb2.RiskSignal
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    def __init__(self, to_issuer_instrument_key: _Optional[str] = ..., to_issuer_instrument_ref: _Optional[str] = ..., instrument_external_reference: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., amount: _Optional[str] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ..., **kwargs) -> None: ...

class ReceiveValueResponse(_message.Message):
    __slots__ = ("status", "error", "transaction_ref")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ReceiveValueResponse.Status]
        STATUS_SUCCESS: _ClassVar[ReceiveValueResponse.Status]
        STATUS_ERROR: _ClassVar[ReceiveValueResponse.Status]
    STATUS_UNSPECIFIED: ReceiveValueResponse.Status
    STATUS_SUCCESS: ReceiveValueResponse.Status
    STATUS_ERROR: ReceiveValueResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    status: ReceiveValueResponse.Status
    error: _error_pb2.Error
    transaction_ref: str
    def __init__(self, status: _Optional[_Union[ReceiveValueResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., transaction_ref: _Optional[str] = ...) -> None: ...

class GetValueRequest(_message.Message):
    __slots__ = ("global_transaction_id", "transaction_ref")
    GLOBAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    global_transaction_id: str
    transaction_ref: str
    def __init__(self, global_transaction_id: _Optional[str] = ..., transaction_ref: _Optional[str] = ...) -> None: ...

class GetValueResponse(_message.Message):
    __slots__ = ("status", "error", "values", "oldest_transaction_time", "transaction_identifier")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetValueResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetValueResponse.Status]
        STATUS_ERROR: _ClassVar[GetValueResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetValueResponse.Status]
    STATUS_UNSPECIFIED: GetValueResponse.Status
    STATUS_SUCCESS: GetValueResponse.Status
    STATUS_ERROR: GetValueResponse.Status
    STATUS_NOT_FOUND: GetValueResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    OLDEST_TRANSACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    status: GetValueResponse.Status
    error: _error_pb2.Error
    values: _containers.RepeatedCompositeFieldContainer[Value]
    oldest_transaction_time: _timestamp_pb2.Timestamp
    transaction_identifier: _transaction_pb2.TransactionIdentifier
    def __init__(self, status: _Optional[_Union[GetValueResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ..., oldest_transaction_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., transaction_identifier: _Optional[_Union[_transaction_pb2.TransactionIdentifier, _Mapping]] = ...) -> None: ...
