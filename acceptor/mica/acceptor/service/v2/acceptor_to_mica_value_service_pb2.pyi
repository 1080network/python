import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from micashared.common.enums.approvaltype.v1 import approval_type_pb2 as _approval_type_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import line_item_pb2 as _line_item_pb2
from micashared.common.v1 import risk_signals_pb2 as _risk_signals_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionIdentifier(_message.Message):
    __slots__ = ("global_transaction_id", "global_transaction_time", "transaction_key")
    GLOBAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TRANSACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    global_transaction_id: str
    global_transaction_time: _timestamp_pb2.Timestamp
    transaction_key: str
    def __init__(self, global_transaction_id: _Optional[str] = ..., global_transaction_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., transaction_key: _Optional[str] = ...) -> None: ...

class OriginalTransactionIdentifier(_message.Message):
    __slots__ = ("global_transaction_id", "transaction_key")
    GLOBAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    global_transaction_id: str
    transaction_key: str
    def __init__(self, global_transaction_id: _Optional[str] = ..., transaction_key: _Optional[str] = ...) -> None: ...

class DiscountSelection(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class LocationDetails(_message.Message):
    __slots__ = ("organization_key", "organization_ref", "category", "clerk_identifier")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLERK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    category: str
    clerk_identifier: str
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., category: _Optional[str] = ..., clerk_identifier: _Optional[str] = ...) -> None: ...

class AcceptorFee(_message.Message):
    __slots__ = ("amount",)
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: str
    def __init__(self, amount: _Optional[str] = ...) -> None: ...

class ValueMetaData(_message.Message):
    __slots__ = ("key_value_pairs",)
    class KeyValuePair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_VALUE_PAIRS_FIELD_NUMBER: _ClassVar[int]
    key_value_pairs: _containers.RepeatedCompositeFieldContainer[ValueMetaData.KeyValuePair]
    def __init__(self, key_value_pairs: _Optional[_Iterable[_Union[ValueMetaData.KeyValuePair, _Mapping]]] = ...) -> None: ...

class BasketDetails(_message.Message):
    __slots__ = ("order_number", "line_items", "adjustments", "surcharges")
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    SURCHARGES_FIELD_NUMBER: _ClassVar[int]
    order_number: str
    line_items: _containers.RepeatedCompositeFieldContainer[_line_item_pb2.LineItem]
    adjustments: _containers.RepeatedCompositeFieldContainer[_line_item_pb2.Adjustment]
    surcharges: _containers.RepeatedCompositeFieldContainer[_line_item_pb2.Surcharge]
    def __init__(self, order_number: _Optional[str] = ..., line_items: _Optional[_Iterable[_Union[_line_item_pb2.LineItem, _Mapping]]] = ..., adjustments: _Optional[_Iterable[_Union[_line_item_pb2.Adjustment, _Mapping]]] = ..., surcharges: _Optional[_Iterable[_Union[_line_item_pb2.Surcharge, _Mapping]]] = ...) -> None: ...

class ObtainValueRequest(_message.Message):
    __slots__ = ("uuek", "approval_type", "transaction_ref", "currency", "requested_amount", "acceptor_fee", "location_details", "basket_details", "meta_data", "risk_signal")
    UUEK_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FEE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BASKET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    uuek: str
    approval_type: _approval_type_pb2.ApprovalType
    transaction_ref: str
    currency: _currency_pb2.Currency
    requested_amount: str
    acceptor_fee: AcceptorFee
    location_details: LocationDetails
    basket_details: BasketDetails
    meta_data: ValueMetaData
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, uuek: _Optional[str] = ..., approval_type: _Optional[_Union[_approval_type_pb2.ApprovalType, str]] = ..., transaction_ref: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., requested_amount: _Optional[str] = ..., acceptor_fee: _Optional[_Union[AcceptorFee, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., basket_details: _Optional[_Union[BasketDetails, _Mapping]] = ..., meta_data: _Optional[_Union[ValueMetaData, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class ObtainValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "declined", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount", "was_partial")
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        WAS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        was_partial: bool
        def __init__(self, approved_amount: _Optional[str] = ..., was_partial: _Optional[bool] = ...) -> None: ...
    class DeclinedResult(_message.Message):
        __slots__ = ("decline_code", "decline_reason")
        DECLINE_CODE_FIELD_NUMBER: _ClassVar[int]
        DECLINE_REASON_FIELD_NUMBER: _ClassVar[int]
        decline_code: str
        decline_reason: str
        def __init__(self, decline_code: _Optional[str] = ..., decline_reason: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: ObtainValueResponse.ApprovedResult
    declined: ObtainValueResponse.DeclinedResult
    error: ObtainValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[ObtainValueResponse.ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[ObtainValueResponse.DeclinedResult, _Mapping]] = ..., error: _Optional[_Union[ObtainValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class ReverseObtainValueRequest(_message.Message):
    __slots__ = ("original_transaction_identifier", "transaction_ref", "risk_signal")
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    original_transaction_identifier: OriginalTransactionIdentifier
    transaction_ref: str
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ..., transaction_ref: _Optional[str] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class ReverseObtainValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount",)
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        def __init__(self, approved_amount: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: ReverseObtainValueResponse.ApprovedResult
    error: ReverseObtainValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[ReverseObtainValueResponse.ApprovedResult, _Mapping]] = ..., error: _Optional[_Union[ReverseObtainValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class RefundValueRequest(_message.Message):
    __slots__ = ("original_transaction_identifier", "transaction_ref", "currency", "requested_amount", "acceptor_fee", "basket_details", "meta_data", "risk_signal")
    ORIGINAL_TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FEE_FIELD_NUMBER: _ClassVar[int]
    BASKET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    original_transaction_identifier: OriginalTransactionIdentifier
    transaction_ref: str
    currency: _currency_pb2.Currency
    requested_amount: str
    acceptor_fee: AcceptorFee
    basket_details: BasketDetails
    meta_data: ValueMetaData
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, original_transaction_identifier: _Optional[_Union[OriginalTransactionIdentifier, _Mapping]] = ..., transaction_ref: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., requested_amount: _Optional[str] = ..., acceptor_fee: _Optional[_Union[AcceptorFee, _Mapping]] = ..., basket_details: _Optional[_Union[BasketDetails, _Mapping]] = ..., meta_data: _Optional[_Union[ValueMetaData, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class RefundValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount",)
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        def __init__(self, approved_amount: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: RefundValueResponse.ApprovedResult
    error: RefundValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[RefundValueResponse.ApprovedResult, _Mapping]] = ..., error: _Optional[_Union[RefundValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class PayoutValueRequest(_message.Message):
    __slots__ = ("uuek", "approval_type", "transaction_ref", "currency", "requested_amount", "acceptor_fee", "location_details", "basket_details", "meta_data", "risk_signal")
    UUEK_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FEE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BASKET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    uuek: str
    approval_type: _approval_type_pb2.ApprovalType
    transaction_ref: str
    currency: _currency_pb2.Currency
    requested_amount: str
    acceptor_fee: AcceptorFee
    location_details: LocationDetails
    basket_details: BasketDetails
    meta_data: ValueMetaData
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, uuek: _Optional[str] = ..., approval_type: _Optional[_Union[_approval_type_pb2.ApprovalType, str]] = ..., transaction_ref: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., requested_amount: _Optional[str] = ..., acceptor_fee: _Optional[_Union[AcceptorFee, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., basket_details: _Optional[_Union[BasketDetails, _Mapping]] = ..., meta_data: _Optional[_Union[ValueMetaData, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class PayoutValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "declined", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount", "was_partial")
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        WAS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        was_partial: bool
        def __init__(self, approved_amount: _Optional[str] = ..., was_partial: _Optional[bool] = ...) -> None: ...
    class DeclinedResult(_message.Message):
        __slots__ = ("decline_code", "decline_reason")
        DECLINE_CODE_FIELD_NUMBER: _ClassVar[int]
        DECLINE_REASON_FIELD_NUMBER: _ClassVar[int]
        decline_code: str
        decline_reason: str
        def __init__(self, decline_code: _Optional[str] = ..., decline_reason: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: PayoutValueResponse.ApprovedResult
    declined: PayoutValueResponse.DeclinedResult
    error: PayoutValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[PayoutValueResponse.ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[PayoutValueResponse.DeclinedResult, _Mapping]] = ..., error: _Optional[_Union[PayoutValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class HoldValueRequest(_message.Message):
    __slots__ = ("uuek", "approval_type", "transaction_ref", "expiration", "currency", "total_amount", "acceptor_fee", "location_details", "basket_details", "risk_signal")
    UUEK_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FEE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BASKET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    uuek: str
    approval_type: _approval_type_pb2.ApprovalType
    transaction_ref: str
    expiration: _timestamp_pb2.Timestamp
    currency: _currency_pb2.Currency
    total_amount: str
    acceptor_fee: AcceptorFee
    location_details: LocationDetails
    basket_details: BasketDetails
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, uuek: _Optional[str] = ..., approval_type: _Optional[_Union[_approval_type_pb2.ApprovalType, str]] = ..., transaction_ref: _Optional[str] = ..., expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., total_amount: _Optional[str] = ..., acceptor_fee: _Optional[_Union[AcceptorFee, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., basket_details: _Optional[_Union[BasketDetails, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class HoldValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "declined", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount", "was_partial")
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        WAS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        was_partial: bool
        def __init__(self, approved_amount: _Optional[str] = ..., was_partial: _Optional[bool] = ...) -> None: ...
    class DeclinedResult(_message.Message):
        __slots__ = ("decline_code", "decline_reason")
        DECLINE_CODE_FIELD_NUMBER: _ClassVar[int]
        DECLINE_REASON_FIELD_NUMBER: _ClassVar[int]
        decline_code: str
        decline_reason: str
        def __init__(self, decline_code: _Optional[str] = ..., decline_reason: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: HoldValueResponse.ApprovedResult
    declined: HoldValueResponse.DeclinedResult
    error: HoldValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[HoldValueResponse.ApprovedResult, _Mapping]] = ..., declined: _Optional[_Union[HoldValueResponse.DeclinedResult, _Mapping]] = ..., error: _Optional[_Union[HoldValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class ReleaseHoldValueRequest(_message.Message):
    __slots__ = ("hold_transaction_key", "hold_transaction_ref", "transaction_ref", "risk_signal")
    HOLD_TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    HOLD_TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    hold_transaction_key: str
    hold_transaction_ref: str
    transaction_ref: str
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, hold_transaction_key: _Optional[str] = ..., hold_transaction_ref: _Optional[str] = ..., transaction_ref: _Optional[str] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class ReleaseHoldValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount",)
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        def __init__(self, approved_amount: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: ReleaseHoldValueResponse.ApprovedResult
    error: ReleaseHoldValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[ReleaseHoldValueResponse.ApprovedResult, _Mapping]] = ..., error: _Optional[_Union[ReleaseHoldValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...

class ObtainHoldValueRequest(_message.Message):
    __slots__ = ("hold_transaction_key", "hold_transaction_ref", "transaction_ref", "currency", "total_amount", "acceptor_fee", "location_details", "basket_details", "risk_signal")
    HOLD_TRANSACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    HOLD_TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_FEE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BASKET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RISK_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    hold_transaction_key: str
    hold_transaction_ref: str
    transaction_ref: str
    currency: _currency_pb2.Currency
    total_amount: str
    acceptor_fee: AcceptorFee
    location_details: LocationDetails
    basket_details: BasketDetails
    risk_signal: _risk_signals_pb2.RiskSignal
    def __init__(self, hold_transaction_key: _Optional[str] = ..., hold_transaction_ref: _Optional[str] = ..., transaction_ref: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., total_amount: _Optional[str] = ..., acceptor_fee: _Optional[_Union[AcceptorFee, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ..., basket_details: _Optional[_Union[BasketDetails, _Mapping]] = ..., risk_signal: _Optional[_Union[_risk_signals_pb2.RiskSignal, _Mapping]] = ...) -> None: ...

class ObtainHoldValueResponse(_message.Message):
    __slots__ = ("transaction_identifier", "cid", "approved", "error")
    class ApprovedResult(_message.Message):
        __slots__ = ("approved_amount",)
        APPROVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        approved_amount: str
        def __init__(self, approved_amount: _Optional[str] = ...) -> None: ...
    class ErrorResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.Error
        def __init__(self, error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: TransactionIdentifier
    cid: str
    approved: ObtainHoldValueResponse.ApprovedResult
    error: ObtainHoldValueResponse.ErrorResult
    def __init__(self, transaction_identifier: _Optional[_Union[TransactionIdentifier, _Mapping]] = ..., cid: _Optional[str] = ..., approved: _Optional[_Union[ObtainHoldValueResponse.ApprovedResult, _Mapping]] = ..., error: _Optional[_Union[ObtainHoldValueResponse.ErrorResult, _Mapping]] = ...) -> None: ...
