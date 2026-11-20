from mica.acceptor.instrument.v2 import instrument_pb2 as _instrument_pb2
from micashared.common.v1 import instrument_pb2 as _instrument_pb2_1
from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteLinkingWithCodeRequest(_message.Message):
    __slots__ = ("linking_code", "organization_key", "organization_ref", "create_uuek")
    LINKING_CODE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    CREATE_UUEK_FIELD_NUMBER: _ClassVar[int]
    linking_code: str
    organization_key: str
    organization_ref: str
    create_uuek: bool
    def __init__(self, linking_code: _Optional[str] = ..., organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., create_uuek: _Optional[bool] = ...) -> None: ...

class CompleteLinkingWithCodeResponse(_message.Message):
    __slots__ = ("is_one_time_use", "link_key", "uuek", "link_name", "claims")
    IS_ONE_TIME_USE_FIELD_NUMBER: _ClassVar[int]
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    UUEK_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    is_one_time_use: bool
    link_key: str
    uuek: str
    link_name: str
    claims: _instrument_pb2_1.InstrumentLinkClaims
    def __init__(self, is_one_time_use: _Optional[bool] = ..., link_key: _Optional[str] = ..., uuek: _Optional[str] = ..., link_name: _Optional[str] = ..., claims: _Optional[_Union[_instrument_pb2_1.InstrumentLinkClaims, _Mapping]] = ...) -> None: ...

class ProvisionUUEKFromLinkRequest(_message.Message):
    __slots__ = ("link_key", "obtain_value", "return_value", "hold_value", "create_recurring_payment")
    class ObtainValueIntent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ReturnValueIntent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class HoldValueIntent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateRecurringPaymentIntent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    RETURN_VALUE_FIELD_NUMBER: _ClassVar[int]
    HOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATE_RECURRING_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    obtain_value: ProvisionUUEKFromLinkRequest.ObtainValueIntent
    return_value: ProvisionUUEKFromLinkRequest.ReturnValueIntent
    hold_value: ProvisionUUEKFromLinkRequest.HoldValueIntent
    create_recurring_payment: ProvisionUUEKFromLinkRequest.CreateRecurringPaymentIntent
    def __init__(self, link_key: _Optional[str] = ..., obtain_value: _Optional[_Union[ProvisionUUEKFromLinkRequest.ObtainValueIntent, _Mapping]] = ..., return_value: _Optional[_Union[ProvisionUUEKFromLinkRequest.ReturnValueIntent, _Mapping]] = ..., hold_value: _Optional[_Union[ProvisionUUEKFromLinkRequest.HoldValueIntent, _Mapping]] = ..., create_recurring_payment: _Optional[_Union[ProvisionUUEKFromLinkRequest.CreateRecurringPaymentIntent, _Mapping]] = ...) -> None: ...

class ProvisionUUEKFromLinkResponse(_message.Message):
    __slots__ = ("uuek",)
    UUEK_FIELD_NUMBER: _ClassVar[int]
    uuek: str
    def __init__(self, uuek: _Optional[str] = ...) -> None: ...
