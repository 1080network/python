import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.common.v1 import currency_pb2 as _currency_pb2
from micashared.common.v1 import instrument_pb2 as _instrument_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterInstrumentRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref", "issuer_instrument_ref", "instrument_type", "nickname", "currency", "adjudication_program_codes")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ADJUDICATION_PROGRAM_CODES_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    issuer_instrument_ref: str
    instrument_type: str
    nickname: str
    currency: _currency_pb2.Currency
    adjudication_program_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ..., instrument_type: _Optional[str] = ..., nickname: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ..., adjudication_program_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class RegisterInstrumentResponse(_message.Message):
    __slots__ = ("status", "error", "issuer_instrument_key", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[RegisterInstrumentResponse.Status]
        STATUS_SUCCESS: _ClassVar[RegisterInstrumentResponse.Status]
        STATUS_ERROR: _ClassVar[RegisterInstrumentResponse.Status]
        STATUS_DUPLICATE: _ClassVar[RegisterInstrumentResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[RegisterInstrumentResponse.Status]
    STATUS_UNSPECIFIED: RegisterInstrumentResponse.Status
    STATUS_SUCCESS: RegisterInstrumentResponse.Status
    STATUS_ERROR: RegisterInstrumentResponse.Status
    STATUS_DUPLICATE: RegisterInstrumentResponse.Status
    STATUS_NOT_FOUND: RegisterInstrumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: RegisterInstrumentResponse.Status
    error: _error_pb2.Error
    issuer_instrument_key: str
    version: int
    def __init__(self, status: _Optional[_Union[RegisterInstrumentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., issuer_instrument_key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class InstrumentExternalReference(_message.Message):
    __slots__ = ("issuer_user_ref", "issuer_instrument_ref")
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    issuer_user_ref: str
    issuer_instrument_ref: str
    def __init__(self, issuer_user_ref: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ...) -> None: ...

class GetInstrumentRequest(_message.Message):
    __slots__ = ("issuer_instrument_key", "external_reference")
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    issuer_instrument_key: str
    external_reference: InstrumentExternalReference
    def __init__(self, issuer_instrument_key: _Optional[str] = ..., external_reference: _Optional[_Union[InstrumentExternalReference, _Mapping]] = ...) -> None: ...

class Instrument(_message.Message):
    __slots__ = ("issuer_instrument_key", "version", "created", "updated", "issuer_instrument_ref", "issuer_user_key", "issuer_user_ref", "instrument_type", "nickname", "currency")
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    issuer_instrument_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    issuer_instrument_ref: str
    issuer_user_key: str
    issuer_user_ref: str
    instrument_type: str
    nickname: str
    currency: _currency_pb2.Currency
    def __init__(self, issuer_instrument_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., issuer_instrument_ref: _Optional[str] = ..., issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., instrument_type: _Optional[str] = ..., nickname: _Optional[str] = ..., currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ...) -> None: ...

class GetInstrumentResponse(_message.Message):
    __slots__ = ("status", "error", "instrument")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetInstrumentResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetInstrumentResponse.Status]
        STATUS_ERROR: _ClassVar[GetInstrumentResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetInstrumentResponse.Status]
    STATUS_UNSPECIFIED: GetInstrumentResponse.Status
    STATUS_SUCCESS: GetInstrumentResponse.Status
    STATUS_ERROR: GetInstrumentResponse.Status
    STATUS_NOT_FOUND: GetInstrumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    status: GetInstrumentResponse.Status
    error: _error_pb2.Error
    instrument: Instrument
    def __init__(self, status: _Optional[_Union[GetInstrumentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., instrument: _Optional[_Union[Instrument, _Mapping]] = ...) -> None: ...

class RemoveInstrumentRequest(_message.Message):
    __slots__ = ("issuer_instrument_key", "external_reference")
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    issuer_instrument_key: str
    external_reference: InstrumentExternalReference
    def __init__(self, issuer_instrument_key: _Optional[str] = ..., external_reference: _Optional[_Union[InstrumentExternalReference, _Mapping]] = ...) -> None: ...

class RemoveInstrumentResponse(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[RemoveInstrumentResponse.Status]
        STATUS_SUCCESS: _ClassVar[RemoveInstrumentResponse.Status]
        STATUS_ERROR: _ClassVar[RemoveInstrumentResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[RemoveInstrumentResponse.Status]
    STATUS_UNSPECIFIED: RemoveInstrumentResponse.Status
    STATUS_SUCCESS: RemoveInstrumentResponse.Status
    STATUS_ERROR: RemoveInstrumentResponse.Status
    STATUS_NOT_FOUND: RemoveInstrumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: RemoveInstrumentResponse.Status
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[RemoveInstrumentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...

class SearchInstrumentRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ...) -> None: ...

class SearchInstrumentResponse(_message.Message):
    __slots__ = ("status", "error", "instruments")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchInstrumentResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchInstrumentResponse.Status]
        STATUS_ERROR: _ClassVar[SearchInstrumentResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[SearchInstrumentResponse.Status]
    STATUS_UNSPECIFIED: SearchInstrumentResponse.Status
    STATUS_SUCCESS: SearchInstrumentResponse.Status
    STATUS_ERROR: SearchInstrumentResponse.Status
    STATUS_NOT_FOUND: SearchInstrumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    status: SearchInstrumentResponse.Status
    error: _error_pb2.Error
    instruments: _containers.RepeatedCompositeFieldContainer[Instrument]
    def __init__(self, status: _Optional[_Union[SearchInstrumentResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., instruments: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ...) -> None: ...

class ProvisionInstrumentLinkingCodeRequest(_message.Message):
    __slots__ = ("issuer_user_ref", "issuer_user_key", "issuer_instrument_ref", "issuer_instrument_key", "claims", "usage_profile")
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    USAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    issuer_user_ref: str
    issuer_user_key: str
    issuer_instrument_ref: str
    issuer_instrument_key: str
    claims: _instrument_pb2.InstrumentLinkClaims
    usage_profile: LinkUsageProfile
    def __init__(self, issuer_user_ref: _Optional[str] = ..., issuer_user_key: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ..., issuer_instrument_key: _Optional[str] = ..., claims: _Optional[_Union[_instrument_pb2.InstrumentLinkClaims, _Mapping]] = ..., usage_profile: _Optional[_Union[LinkUsageProfile, _Mapping]] = ...) -> None: ...

class ProvisionInstrumentLinkingCodeResponse(_message.Message):
    __slots__ = ("status", "error", "linking_code")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ProvisionInstrumentLinkingCodeResponse.Status]
        STATUS_SUCCESS: _ClassVar[ProvisionInstrumentLinkingCodeResponse.Status]
        STATUS_ERROR: _ClassVar[ProvisionInstrumentLinkingCodeResponse.Status]
        STATUS_INSTRUMENT_NOT_FOUND: _ClassVar[ProvisionInstrumentLinkingCodeResponse.Status]
        STATUS_USER_NOT_FOUND: _ClassVar[ProvisionInstrumentLinkingCodeResponse.Status]
    STATUS_UNSPECIFIED: ProvisionInstrumentLinkingCodeResponse.Status
    STATUS_SUCCESS: ProvisionInstrumentLinkingCodeResponse.Status
    STATUS_ERROR: ProvisionInstrumentLinkingCodeResponse.Status
    STATUS_INSTRUMENT_NOT_FOUND: ProvisionInstrumentLinkingCodeResponse.Status
    STATUS_USER_NOT_FOUND: ProvisionInstrumentLinkingCodeResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LINKING_CODE_FIELD_NUMBER: _ClassVar[int]
    status: ProvisionInstrumentLinkingCodeResponse.Status
    error: _error_pb2.Error
    linking_code: str
    def __init__(self, status: _Optional[_Union[ProvisionInstrumentLinkingCodeResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., linking_code: _Optional[str] = ...) -> None: ...

class CompleteLinkingWithCodeRequest(_message.Message):
    __slots__ = ("linking_code", "user_ref", "user_key", "instrument_ref", "instrument_key")
    LINKING_CODE_FIELD_NUMBER: _ClassVar[int]
    USER_REF_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    linking_code: str
    user_ref: str
    user_key: str
    instrument_ref: str
    instrument_key: str
    def __init__(self, linking_code: _Optional[str] = ..., user_ref: _Optional[str] = ..., user_key: _Optional[str] = ..., instrument_ref: _Optional[str] = ..., instrument_key: _Optional[str] = ...) -> None: ...

class CompleteLinkingWithCodeResponse(_message.Message):
    __slots__ = ("status", "error", "instrument_link", "claims")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_SUCCESS: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_INVALID_NETWORK: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_UNSUPPORTED_LINK_SOURCE: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_USER_NOT_FOUND: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_INSTRUMENT_NOT_FOUND: _ClassVar[CompleteLinkingWithCodeResponse.Status]
        STATUS_INVALID_CODE: _ClassVar[CompleteLinkingWithCodeResponse.Status]
    STATUS_UNSPECIFIED: CompleteLinkingWithCodeResponse.Status
    STATUS_SUCCESS: CompleteLinkingWithCodeResponse.Status
    STATUS_INVALID_NETWORK: CompleteLinkingWithCodeResponse.Status
    STATUS_UNSUPPORTED_LINK_SOURCE: CompleteLinkingWithCodeResponse.Status
    STATUS_USER_NOT_FOUND: CompleteLinkingWithCodeResponse.Status
    STATUS_INSTRUMENT_NOT_FOUND: CompleteLinkingWithCodeResponse.Status
    STATUS_INVALID_CODE: CompleteLinkingWithCodeResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    status: CompleteLinkingWithCodeResponse.Status
    error: _error_pb2.Error
    instrument_link: InstrumentLink
    claims: _instrument_pb2.InstrumentLinkClaims
    def __init__(self, status: _Optional[_Union[CompleteLinkingWithCodeResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., instrument_link: _Optional[_Union[InstrumentLink, _Mapping]] = ..., claims: _Optional[_Union[_instrument_pb2.InstrumentLinkClaims, _Mapping]] = ...) -> None: ...

class GetInstrumentLinkRequest(_message.Message):
    __slots__ = ("link_key",)
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    def __init__(self, link_key: _Optional[str] = ...) -> None: ...

class GetInstrumentLinkResponse(_message.Message):
    __slots__ = ("status", "error", "instrument_link")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetInstrumentLinkResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetInstrumentLinkResponse.Status]
        STATUS_LINK_NOT_FOUND: _ClassVar[GetInstrumentLinkResponse.Status]
    STATUS_UNSPECIFIED: GetInstrumentLinkResponse.Status
    STATUS_SUCCESS: GetInstrumentLinkResponse.Status
    STATUS_LINK_NOT_FOUND: GetInstrumentLinkResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    status: GetInstrumentLinkResponse.Status
    error: _error_pb2.Error
    instrument_link: InstrumentLink
    def __init__(self, status: _Optional[_Union[GetInstrumentLinkResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., instrument_link: _Optional[_Union[InstrumentLink, _Mapping]] = ...) -> None: ...

class SearchInstrumentLinksRequest(_message.Message):
    __slots__ = ("user_ref", "user_key", "instrument_ref", "instrument_key")
    USER_REF_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    user_ref: str
    user_key: str
    instrument_ref: str
    instrument_key: str
    def __init__(self, user_ref: _Optional[str] = ..., user_key: _Optional[str] = ..., instrument_ref: _Optional[str] = ..., instrument_key: _Optional[str] = ...) -> None: ...

class SearchInstrumentLinksResponse(_message.Message):
    __slots__ = ("status", "error", "instrument_links")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchInstrumentLinksResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchInstrumentLinksResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[SearchInstrumentLinksResponse.Status]
    STATUS_UNSPECIFIED: SearchInstrumentLinksResponse.Status
    STATUS_SUCCESS: SearchInstrumentLinksResponse.Status
    STATUS_NOT_FOUND: SearchInstrumentLinksResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_LINKS_FIELD_NUMBER: _ClassVar[int]
    status: SearchInstrumentLinksResponse.Status
    error: _error_pb2.Error
    instrument_links: _containers.RepeatedCompositeFieldContainer[InstrumentLink]
    def __init__(self, status: _Optional[_Union[SearchInstrumentLinksResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., instrument_links: _Optional[_Iterable[_Union[InstrumentLink, _Mapping]]] = ...) -> None: ...

class RemoveInstrumentLinkRequest(_message.Message):
    __slots__ = ("link_key",)
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    def __init__(self, link_key: _Optional[str] = ...) -> None: ...

class RemoveInstrumentLinkResponse(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[RemoveInstrumentLinkResponse.Status]
        STATUS_SUCCESS: _ClassVar[RemoveInstrumentLinkResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[RemoveInstrumentLinkResponse.Status]
        STATUS_LINK_IN_USE: _ClassVar[RemoveInstrumentLinkResponse.Status]
    STATUS_UNSPECIFIED: RemoveInstrumentLinkResponse.Status
    STATUS_SUCCESS: RemoveInstrumentLinkResponse.Status
    STATUS_NOT_FOUND: RemoveInstrumentLinkResponse.Status
    STATUS_LINK_IN_USE: RemoveInstrumentLinkResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: RemoveInstrumentLinkResponse.Status
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[RemoveInstrumentLinkResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...

class LinkUsageProfile(_message.Message):
    __slots__ = ("for_one_time_use",)
    FOR_ONE_TIME_USE_FIELD_NUMBER: _ClassVar[int]
    for_one_time_use: bool
    def __init__(self, for_one_time_use: _Optional[bool] = ...) -> None: ...

class InstrumentLink(_message.Message):
    __slots__ = ("link_key", "version", "created", "updated", "issuer_user_key", "issuer_user_ref", "issuer_instrument_ref", "issuer_instrument_key", "organization_name", "organization_icon_url", "linked_instrument_data")
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_REF_FIELD_NUMBER: _ClassVar[int]
    ISSUER_INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ICON_URL_FIELD_NUMBER: _ClassVar[int]
    LINKED_INSTRUMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    issuer_user_key: str
    issuer_user_ref: str
    issuer_instrument_ref: str
    issuer_instrument_key: str
    organization_name: str
    organization_icon_url: str
    linked_instrument_data: _instrument_pb2.LinkedInstrumentData
    def __init__(self, link_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., issuer_instrument_ref: _Optional[str] = ..., issuer_instrument_key: _Optional[str] = ..., organization_name: _Optional[str] = ..., organization_icon_url: _Optional[str] = ..., linked_instrument_data: _Optional[_Union[_instrument_pb2.LinkedInstrumentData, _Mapping]] = ...) -> None: ...
