import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.enums.ageband.v1 import age_band_pb2 as _age_band_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("region_code", "country_code")
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    region_code: str
    country_code: str
    def __init__(self, region_code: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

class UserDemographic(_message.Message):
    __slots__ = ("address", "age_band")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AGE_BAND_FIELD_NUMBER: _ClassVar[int]
    address: Address
    age_band: _age_band_pb2.AgeBand
    def __init__(self, address: _Optional[_Union[Address, _Mapping]] = ..., age_band: _Optional[_Union[_age_band_pb2.AgeBand, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("version", "created", "updated", "issuer_user_key", "issuer_user_ref", "user_demographic")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    USER_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    issuer_user_key: str
    issuer_user_ref: str
    user_demographic: UserDemographic
    def __init__(self, version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., user_demographic: _Optional[_Union[UserDemographic, _Mapping]] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ("issuer_user_ref", "user_demographic")
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    USER_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    issuer_user_ref: str
    user_demographic: UserDemographic
    def __init__(self, issuer_user_ref: _Optional[str] = ..., user_demographic: _Optional[_Union[UserDemographic, _Mapping]] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ("status", "error", "issuer_user_key", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[RegisterUserResponse.Status]
        STATUS_SUCCESS: _ClassVar[RegisterUserResponse.Status]
        STATUS_ERROR: _ClassVar[RegisterUserResponse.Status]
        STATUS_DUPLICATE: _ClassVar[RegisterUserResponse.Status]
    STATUS_UNSPECIFIED: RegisterUserResponse.Status
    STATUS_SUCCESS: RegisterUserResponse.Status
    STATUS_ERROR: RegisterUserResponse.Status
    STATUS_DUPLICATE: RegisterUserResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: RegisterUserResponse.Status
    error: _error_pb2.Error
    issuer_user_key: str
    version: int
    def __init__(self, status: _Optional[_Union[RegisterUserResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., issuer_user_key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref", "version", "user_demographic")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    version: int
    user_demographic: UserDemographic
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ..., version: _Optional[int] = ..., user_demographic: _Optional[_Union[UserDemographic, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateUserResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateUserResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateUserResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[UpdateUserResponse.Status]
        STATUS_VERSION_MISMATCH: _ClassVar[UpdateUserResponse.Status]
    STATUS_UNSPECIFIED: UpdateUserResponse.Status
    STATUS_SUCCESS: UpdateUserResponse.Status
    STATUS_ERROR: UpdateUserResponse.Status
    STATUS_NOT_FOUND: UpdateUserResponse.Status
    STATUS_VERSION_MISMATCH: UpdateUserResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: UpdateUserResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[UpdateUserResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class RemoveUserRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ...) -> None: ...

class RemoveUserResponse(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[RemoveUserResponse.Status]
        STATUS_SUCCESS: _ClassVar[RemoveUserResponse.Status]
        STATUS_ERROR: _ClassVar[RemoveUserResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[RemoveUserResponse.Status]
    STATUS_UNSPECIFIED: RemoveUserResponse.Status
    STATUS_SUCCESS: RemoveUserResponse.Status
    STATUS_ERROR: RemoveUserResponse.Status
    STATUS_NOT_FOUND: RemoveUserResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: RemoveUserResponse.Status
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[RemoveUserResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("issuer_user_key", "issuer_user_ref")
    ISSUER_USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUER_USER_REF_FIELD_NUMBER: _ClassVar[int]
    issuer_user_key: str
    issuer_user_ref: str
    def __init__(self, issuer_user_key: _Optional[str] = ..., issuer_user_ref: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("status", "error", "user")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetUserResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetUserResponse.Status]
        STATUS_ERROR: _ClassVar[GetUserResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetUserResponse.Status]
    STATUS_UNSPECIFIED: GetUserResponse.Status
    STATUS_SUCCESS: GetUserResponse.Status
    STATUS_ERROR: GetUserResponse.Status
    STATUS_NOT_FOUND: GetUserResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    status: GetUserResponse.Status
    error: _error_pb2.Error
    user: User
    def __init__(self, status: _Optional[_Union[GetUserResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...
