import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from micashared.common.v1 import bank_account_detail_pb2 as _bank_account_detail_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Issuer(_message.Message):
    __slots__ = ("issuer_key", "version", "created", "updated", "name", "issuer_url", "operating_account", "revenue_account", "network_group", "features")
    ISSUER_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    OPERATING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REVENUE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_GROUP_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    issuer_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    name: str
    issuer_url: str
    operating_account: _bank_account_detail_pb2.BankAccountDetail
    revenue_account: _bank_account_detail_pb2.BankAccountDetail
    network_group: str
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, issuer_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., issuer_url: _Optional[str] = ..., operating_account: _Optional[_Union[_bank_account_detail_pb2.BankAccountDetail, _Mapping]] = ..., revenue_account: _Optional[_Union[_bank_account_detail_pb2.BankAccountDetail, _Mapping]] = ..., network_group: _Optional[str] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...

class GetIssuerRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIssuerResponse(_message.Message):
    __slots__ = ("status", "error", "issuer")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetIssuerResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetIssuerResponse.Status]
        STATUS_ERROR: _ClassVar[GetIssuerResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetIssuerResponse.Status]
    STATUS_UNSPECIFIED: GetIssuerResponse.Status
    STATUS_SUCCESS: GetIssuerResponse.Status
    STATUS_ERROR: GetIssuerResponse.Status
    STATUS_NOT_FOUND: GetIssuerResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    status: GetIssuerResponse.Status
    error: _error_pb2.Error
    issuer: Issuer
    def __init__(self, status: _Optional[_Union[GetIssuerResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., issuer: _Optional[_Union[Issuer, _Mapping]] = ...) -> None: ...
