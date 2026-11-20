from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ABAAccountNumber(_message.Message):
    __slots__ = ("name", "routing_number", "account_number")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    routing_number: str
    account_number: str
    def __init__(self, name: _Optional[str] = ..., routing_number: _Optional[str] = ..., account_number: _Optional[str] = ...) -> None: ...

class BankAccountDetail(_message.Message):
    __slots__ = ("bank", "account_ref")
    BANK_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_REF_FIELD_NUMBER: _ClassVar[int]
    bank: str
    account_ref: str
    def __init__(self, bank: _Optional[str] = ..., account_ref: _Optional[str] = ...) -> None: ...

class ABAAccountEntry(_message.Message):
    __slots__ = ("key", "version", "enabled", "account_detail")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    key: str
    version: int
    enabled: bool
    account_detail: ABAAccountNumber
    def __init__(self, key: _Optional[str] = ..., version: _Optional[int] = ..., enabled: _Optional[bool] = ..., account_detail: _Optional[_Union[ABAAccountNumber, _Mapping]] = ...) -> None: ...
