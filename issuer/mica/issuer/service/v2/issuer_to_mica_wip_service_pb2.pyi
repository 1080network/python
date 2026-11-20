import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from mica.issuer.instrument.v2 import instrument_pb2 as _instrument_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import risk_signals_pb2 as _risk_signals_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecurringPayment(_message.Message):
    __slots__ = ("recurring_payment_key", "nickname", "instrument_key", "instrument_external_ref", "currency", "created_at", "usage", "terms")
    RECURRING_PAYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXTERNAL_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TERMS_FIELD_NUMBER: _ClassVar[int]
    recurring_payment_key: str
    nickname: str
    instrument_key: str
    instrument_external_ref: _instrument_pb2.InstrumentExternalReference
    currency: _currency_pb2.Currency
    created_at: _timestamp_pb2.Timestamp
    usage: RecurringPaymentUsage
    terms: RecurringPaymentTerms
    def __init__(self, recurring_payment_key: _Optional[str] = ..., nickname: _Optional[str] = ..., instrument_key: _Optional[str] = ..., instrument_external_ref: _Optional[_Union[_instrument_pb2.InstrumentExternalReference, _Mapping]] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., usage: _Optional[_Union[RecurringPaymentUsage, _Mapping]] = ..., terms: _Optional[_Union[RecurringPaymentTerms, _Mapping]] = ...) -> None: ...

class RecurringPaymentUsage(_message.Message):
    __slots__ = ("last_payment", "last_payment_amount", "number_of_payments_made", "total_payment_amount")
    LAST_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    LAST_PAYMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_PAYMENTS_MADE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAYMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    last_payment: _timestamp_pb2.Timestamp
    last_payment_amount: str
    number_of_payments_made: int
    total_payment_amount: str
    def __init__(self, last_payment: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_payment_amount: _Optional[str] = ..., number_of_payments_made: _Optional[int] = ..., total_payment_amount: _Optional[str] = ...) -> None: ...

class RecurringPaymentTerms(_message.Message):
    __slots__ = ("total_spend_limit",)
    TOTAL_SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    total_spend_limit: str
    def __init__(self, total_spend_limit: _Optional[str] = ...) -> None: ...

class SearchRecurringPaymentsRequest(_message.Message):
    __slots__ = ("user",)
    class ByUser(_message.Message):
        __slots__ = ("user_ref", "user_key")
        USER_REF_FIELD_NUMBER: _ClassVar[int]
        USER_KEY_FIELD_NUMBER: _ClassVar[int]
        user_ref: str
        user_key: str
        def __init__(self, user_ref: _Optional[str] = ..., user_key: _Optional[str] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    user: SearchRecurringPaymentsRequest.ByUser
    def __init__(self, user: _Optional[_Union[SearchRecurringPaymentsRequest.ByUser, _Mapping]] = ...) -> None: ...

class SearchRecurringPaymentsResponse(_message.Message):
    __slots__ = ("status", "error", "recurring_payments")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchRecurringPaymentsResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchRecurringPaymentsResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[SearchRecurringPaymentsResponse.Status]
    STATUS_UNSPECIFIED: SearchRecurringPaymentsResponse.Status
    STATUS_SUCCESS: SearchRecurringPaymentsResponse.Status
    STATUS_NOT_FOUND: SearchRecurringPaymentsResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECURRING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    status: SearchRecurringPaymentsResponse.Status
    error: _error_pb2.Error
    recurring_payments: _containers.RepeatedCompositeFieldContainer[RecurringPayment]
    def __init__(self, status: _Optional[_Union[SearchRecurringPaymentsResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., recurring_payments: _Optional[_Iterable[_Union[RecurringPayment, _Mapping]]] = ...) -> None: ...

class SendValueRequest(_message.Message):
    __slots__ = ("from_issuer_user_key", "issuer_user_key", "issuer_user_ref", "from_issuer_instrument_key", "issuer_instrument_key", "issuer_instrument_ref", "to_uuek", "currency", "amount", "risk_signal")
    FROM_ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    FROM_ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    TO_UUEK_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    from_issuer_user_key: str
    issuer_user_key: str
    issuer_user_ref: str
    from_issuer_instrument_key: str
    issuer_instrument_key: str
    issuer_instrument_ref: str
    to_uuek: str
    currency: _currency_pb2.Currency
    amount: str
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, from_issuer_user_key: _Optional[str] = ..., issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., from_issuer_instrument_key: _Optional[str] = ..., issuer_instrument_key: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ..., to_uuek: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., amount: _Optional[str] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class SendValueResponse(_message.Message):
    __slots__ = ("status", "error", "transaction_key")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SendValueResponse.Status]
        STATUS_SUCCESS: _ClassVar[SendValueResponse.Status]
        STATUS_ERROR: _ClassVar[SendValueResponse.Status]
    STATUS_UNSPECIFIED: SendValueResponse.Status
    STATUS_SUCCESS: SendValueResponse.Status
    STATUS_ERROR: SendValueResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    status: SendValueResponse.Status
    error: _error_pb2.Error
    transaction_key: str
    def __init__(self, status: _Optional[_Union[SendValueResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., transaction_key: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("street_lines", "locality", "region_code", "postal_code", "country_code")
    STREET_LINES_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    street_lines: _containers.RepeatedScalarFieldContainer[str]
    locality: str
    region_code: str
    postal_code: str
    country_code: str
    def __init__(self, street_lines: _Optional[_Iterable[str]] = ..., locality: _Optional[str] = ..., region_code: _Optional[str] = ..., postal_code: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

class UserDemographic(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "address", "phone", "username")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    address: Address
    phone: str
    username: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., phone: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class InitializeWebSessionRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref", "user_demographic", "meta_data")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    USER_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    user_demographic: UserDemographic
    meta_data: WebSessionMetaData
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., user_demographic: _Optional[_Union[UserDemographic, _Mapping]] = ..., meta_data: _Optional[_Union[WebSessionMetaData, _Mapping]] = ...) -> None: ...

class InitializeWebSessionResponse(_message.Message):
    __slots__ = ("token", "expires_at")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    token: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WebSessionMetaData(_message.Message):
    __slots__ = ("key_value_pairs",)
    class KeyValuePair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_VALUE_PAIRS_FIELD_NUMBER: _ClassVar[int]
    key_value_pairs: _containers.RepeatedCompositeFieldContainer[WebSessionMetaData.KeyValuePair]
    def __init__(self, key_value_pairs: _Optional[_Iterable[_Union[WebSessionMetaData.KeyValuePair, _Mapping]]] = ...) -> None: ...
