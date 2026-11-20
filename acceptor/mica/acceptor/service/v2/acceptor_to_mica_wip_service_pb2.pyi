import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecurringPayment(_message.Message):
    __slots__ = ("recurring_payment_key", "nickname", "currency", "created")
    RECURRING_PAYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    recurring_payment_key: str
    nickname: str
    currency: _currency_pb2.Currency
    created: _timestamp_pb2.Timestamp
    def __init__(self, recurring_payment_key: _Optional[str] = ..., nickname: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RecurringPaymentTerms(_message.Message):
    __slots__ = ("total_spend_limit",)
    TOTAL_SPEND_LIMIT_FIELD_NUMBER: _ClassVar[int]
    total_spend_limit: str
    def __init__(self, total_spend_limit: _Optional[str] = ...) -> None: ...

class CreateRecurringPaymentRequest(_message.Message):
    __slots__ = ("organization_key", "organization_ref", "uuek", "nickname", "currency", "terms")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    UUEK_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TERMS_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    uuek: str
    nickname: str
    currency: _currency_pb2.Currency
    terms: RecurringPaymentTerms
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., uuek: _Optional[str] = ..., nickname: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., terms: _Optional[_Union[RecurringPaymentTerms, _Mapping]] = ...) -> None: ...

class CreateRecurringPaymentResponse(_message.Message):
    __slots__ = ("status", "error", "recurring_payment_key")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[CreateRecurringPaymentResponse.Status]
        STATUS_SUCCESS: _ClassVar[CreateRecurringPaymentResponse.Status]
        STATUS_ERROR: _ClassVar[CreateRecurringPaymentResponse.Status]
    STATUS_UNSPECIFIED: CreateRecurringPaymentResponse.Status
    STATUS_SUCCESS: CreateRecurringPaymentResponse.Status
    STATUS_ERROR: CreateRecurringPaymentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECURRING_PAYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    status: CreateRecurringPaymentResponse.Status
    error: _error_pb2.Error
    recurring_payment_key: str
    def __init__(self, status: _Optional[_Union[CreateRecurringPaymentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., recurring_payment_key: _Optional[str] = ...) -> None: ...

class GetRecurringPaymentRequest(_message.Message):
    __slots__ = ("recurring_payment_key",)
    RECURRING_PAYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    recurring_payment_key: str
    def __init__(self, recurring_payment_key: _Optional[str] = ...) -> None: ...

class GetRecurringPaymentResponse(_message.Message):
    __slots__ = ("status", "error", "recurring_payment")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetRecurringPaymentResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetRecurringPaymentResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetRecurringPaymentResponse.Status]
    STATUS_UNSPECIFIED: GetRecurringPaymentResponse.Status
    STATUS_SUCCESS: GetRecurringPaymentResponse.Status
    STATUS_NOT_FOUND: GetRecurringPaymentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECURRING_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    status: GetRecurringPaymentResponse.Status
    error: _error_pb2.Error
    recurring_payment: RecurringPayment
    def __init__(self, status: _Optional[_Union[GetRecurringPaymentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., recurring_payment: _Optional[_Union[RecurringPayment, _Mapping]] = ...) -> None: ...

class ProvisionRecurringPaymentUUEKRequest(_message.Message):
    __slots__ = ("recurring_payment_key",)
    RECURRING_PAYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    recurring_payment_key: str
    def __init__(self, recurring_payment_key: _Optional[str] = ...) -> None: ...

class ProvisionRecurringPaymentUUEKResponse(_message.Message):
    __slots__ = ("status", "error", "uuek")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ProvisionRecurringPaymentUUEKResponse.Status]
        STATUS_SUCCESS: _ClassVar[ProvisionRecurringPaymentUUEKResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[ProvisionRecurringPaymentUUEKResponse.Status]
    STATUS_UNSPECIFIED: ProvisionRecurringPaymentUUEKResponse.Status
    STATUS_SUCCESS: ProvisionRecurringPaymentUUEKResponse.Status
    STATUS_NOT_FOUND: ProvisionRecurringPaymentUUEKResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UUEK_FIELD_NUMBER: _ClassVar[int]
    status: ProvisionRecurringPaymentUUEKResponse.Status
    error: _error_pb2.Error
    uuek: str
    def __init__(self, status: _Optional[_Union[ProvisionRecurringPaymentUUEKResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., uuek: _Optional[str] = ...) -> None: ...
