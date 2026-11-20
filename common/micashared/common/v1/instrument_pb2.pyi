from micashared.common.enums.ageband.v1 import age_band_pb2 as _age_band_pb2
from micashared.common.v1 import address_pb2 as _address_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinkedInstrumentData(_message.Message):
    __slots__ = ("name", "type", "icon_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    icon_url: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., icon_url: _Optional[str] = ...) -> None: ...

class UserDemographic(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "address", "age_band", "phone")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AGE_BAND_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    address: _address_pb2.Address
    age_band: _age_band_pb2.AgeBand
    phone: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., age_band: _Optional[_Union[_age_band_pb2.AgeBand, str]] = ..., phone: _Optional[str] = ...) -> None: ...

class InstrumentLinkClaims(_message.Message):
    __slots__ = ("assertions", "user_demographic")
    class AssertionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
    USER_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    assertions: _containers.ScalarMap[str, str]
    user_demographic: UserDemographic
    def __init__(self, assertions: _Optional[_Mapping[str, str]] = ..., user_demographic: _Optional[_Union[UserDemographic, _Mapping]] = ...) -> None: ...
