from micashared.common.v1 import error_pb2 as _error_pb2
from micashared.common.v1 import instrument_pb2 as _instrument_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLinkRequest(_message.Message):
    __slots__ = ("link_key",)
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    def __init__(self, link_key: _Optional[str] = ...) -> None: ...

class GetLinkResponse(_message.Message):
    __slots__ = ("status", "error", "link")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetLinkResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetLinkResponse.Status]
        STATUS_LINK_NOT_FOUND: _ClassVar[GetLinkResponse.Status]
    STATUS_UNSPECIFIED: GetLinkResponse.Status
    STATUS_SUCCESS: GetLinkResponse.Status
    STATUS_LINK_NOT_FOUND: GetLinkResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    status: GetLinkResponse.Status
    error: _error_pb2.Error
    link: Link
    def __init__(self, status: _Optional[_Union[GetLinkResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., link: _Optional[_Union[Link, _Mapping]] = ...) -> None: ...

class RemoveInstrumentLinkRequest(_message.Message):
    __slots__ = ("link_key",)
    LINK_KEY_FIELD_NUMBER: _ClassVar[int]
    link_key: str
    def __init__(self, link_key: _Optional[str] = ...) -> None: ...

class RemoveInstrumentLinkResponse(_message.Message):
    __slots__ = ("success", "failure")
    class FailureCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CODE_UNSPECIFIED: _ClassVar[RemoveInstrumentLinkResponse.FailureCode]
        FAILURE_CODE_LINK_NOT_FOUND: _ClassVar[RemoveInstrumentLinkResponse.FailureCode]
        FAILURE_CODE_LINK_IN_USE: _ClassVar[RemoveInstrumentLinkResponse.FailureCode]
    FAILURE_CODE_UNSPECIFIED: RemoveInstrumentLinkResponse.FailureCode
    FAILURE_CODE_LINK_NOT_FOUND: RemoveInstrumentLinkResponse.FailureCode
    FAILURE_CODE_LINK_IN_USE: RemoveInstrumentLinkResponse.FailureCode
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: RemoveInstrumentLinkResponse.FailureCode
        message: str
        def __init__(self, code: _Optional[_Union[RemoveInstrumentLinkResponse.FailureCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RemoveInstrumentLinkResponse.Success
    failure: RemoveInstrumentLinkResponse.Failure
    def __init__(self, success: _Optional[_Union[RemoveInstrumentLinkResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[RemoveInstrumentLinkResponse.Failure, _Mapping]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("key", "instrument_data")
    KEY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    instrument_data: _instrument_pb2.LinkedInstrumentData
    def __init__(self, key: _Optional[str] = ..., instrument_data: _Optional[_Union[_instrument_pb2.LinkedInstrumentData, _Mapping]] = ...) -> None: ...
