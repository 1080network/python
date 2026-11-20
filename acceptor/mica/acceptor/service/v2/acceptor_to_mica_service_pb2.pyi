import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mica.acceptor.acceptor.v2 import acceptor_pb2 as _acceptor_pb2
from micashared.common.enums.organizationstatus.v1 import organization_status_pb2 as _organization_status_pb2
from micashared.common.v1 import address_pb2 as _address_pb2
from micashared.common.v1 import error_pb2 as _error_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("organization_ref", "name", "address", "parent_organization_key", "parent_organization_ref", "categories", "phone")
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    organization_ref: str
    name: str
    address: _address_pb2.Address
    parent_organization_key: str
    parent_organization_ref: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    phone: str
    def __init__(self, organization_ref: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., parent_organization_key: _Optional[str] = ..., parent_organization_ref: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ..., phone: _Optional[str] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "organization_key", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[CreateOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[CreateOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[CreateOrganizationResponse.Status]
        STATUS_DUPLICATE: _ClassVar[CreateOrganizationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[CreateOrganizationResponse.Status]
    STATUS_UNSPECIFIED: CreateOrganizationResponse.Status
    STATUS_SUCCESS: CreateOrganizationResponse.Status
    STATUS_ERROR: CreateOrganizationResponse.Status
    STATUS_DUPLICATE: CreateOrganizationResponse.Status
    STATUS_NOT_FOUND: CreateOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: CreateOrganizationResponse.Status
    error: _error_pb2.Error
    organization_key: str
    version: int
    def __init__(self, status: _Optional[_Union[CreateOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., organization_key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ParentOrganization(_message.Message):
    __slots__ = ("organization_key", "organization_ref")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ("organization_key", "version", "created", "updated", "acceptor_key", "parent_organization", "organization_ref", "name", "status", "address", "categories")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ACCEPTOR_KEY_FIELD_NUMBER: _ClassVar[int]
    PARENT_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    version: int
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    acceptor_key: str
    parent_organization: ParentOrganization
    organization_ref: str
    name: str
    status: _organization_status_pb2.OrganizationStatus
    address: _address_pb2.Address
    categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, organization_key: _Optional[str] = ..., version: _Optional[int] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., acceptor_key: _Optional[str] = ..., parent_organization: _Optional[_Union[ParentOrganization, _Mapping]] = ..., organization_ref: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_organization_status_pb2.OrganizationStatus, str]] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., categories: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ("organization_key", "organization_ref")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ...) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "organization")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[GetOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[GetOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[GetOrganizationResponse.Status]
        STATUS_INVALID_ACCEPTOR_ID: _ClassVar[GetOrganizationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[GetOrganizationResponse.Status]
    STATUS_UNSPECIFIED: GetOrganizationResponse.Status
    STATUS_SUCCESS: GetOrganizationResponse.Status
    STATUS_ERROR: GetOrganizationResponse.Status
    STATUS_INVALID_ACCEPTOR_ID: GetOrganizationResponse.Status
    STATUS_NOT_FOUND: GetOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    status: GetOrganizationResponse.Status
    error: _error_pb2.Error
    organization: Organization
    def __init__(self, status: _Optional[_Union[GetOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("organization_key", "organization_ref", "version", "name", "address", "categories", "phone")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    version: int
    name: str
    address: _address_pb2.Address
    categories: _containers.RepeatedScalarFieldContainer[str]
    phone: str
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., categories: _Optional[_Iterable[str]] = ..., phone: _Optional[str] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpdateOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[UpdateOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[UpdateOrganizationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[UpdateOrganizationResponse.Status]
        STATUS_VERSION_MISMATCH: _ClassVar[UpdateOrganizationResponse.Status]
    STATUS_UNSPECIFIED: UpdateOrganizationResponse.Status
    STATUS_SUCCESS: UpdateOrganizationResponse.Status
    STATUS_ERROR: UpdateOrganizationResponse.Status
    STATUS_NOT_FOUND: UpdateOrganizationResponse.Status
    STATUS_VERSION_MISMATCH: UpdateOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: UpdateOrganizationResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[UpdateOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class ActivateOrganizationRequest(_message.Message):
    __slots__ = ("organization_key", "organization_ref", "version")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    version: int
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ActivateOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_VERSION_MISMATCH: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_INVALID_STATE_TRANSITION: _ClassVar[ActivateOrganizationResponse.Status]
        STATUS_MISSING_ACCOUNT_DETAILS: _ClassVar[ActivateOrganizationResponse.Status]
    STATUS_UNSPECIFIED: ActivateOrganizationResponse.Status
    STATUS_SUCCESS: ActivateOrganizationResponse.Status
    STATUS_ERROR: ActivateOrganizationResponse.Status
    STATUS_NOT_FOUND: ActivateOrganizationResponse.Status
    STATUS_VERSION_MISMATCH: ActivateOrganizationResponse.Status
    STATUS_INVALID_STATE_TRANSITION: ActivateOrganizationResponse.Status
    STATUS_MISSING_ACCOUNT_DETAILS: ActivateOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: ActivateOrganizationResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[ActivateOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class DeactivateOrganizationRequest(_message.Message):
    __slots__ = ("organization_key", "organization_ref", "version")
    ORGANIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    organization_key: str
    organization_ref: str
    version: int
    def __init__(self, organization_key: _Optional[str] = ..., organization_ref: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DeactivateOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "version")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[DeactivateOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[DeactivateOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[DeactivateOrganizationResponse.Status]
        STATUS_NOT_FOUND: _ClassVar[DeactivateOrganizationResponse.Status]
        STATUS_VERSION_MISMATCH: _ClassVar[DeactivateOrganizationResponse.Status]
        STATUS_INVALID_STATE_TRANSITION: _ClassVar[DeactivateOrganizationResponse.Status]
    STATUS_UNSPECIFIED: DeactivateOrganizationResponse.Status
    STATUS_SUCCESS: DeactivateOrganizationResponse.Status
    STATUS_ERROR: DeactivateOrganizationResponse.Status
    STATUS_NOT_FOUND: DeactivateOrganizationResponse.Status
    STATUS_VERSION_MISMATCH: DeactivateOrganizationResponse.Status
    STATUS_INVALID_STATE_TRANSITION: DeactivateOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: DeactivateOrganizationResponse.Status
    error: _error_pb2.Error
    version: int
    def __init__(self, status: _Optional[_Union[DeactivateOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class SearchOrganizationRequest(_message.Message):
    __slots__ = ("name", "category")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    name: str
    category: str
    def __init__(self, name: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class SearchOrganizationResponse(_message.Message):
    __slots__ = ("status", "error", "organizations")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[SearchOrganizationResponse.Status]
        STATUS_SUCCESS: _ClassVar[SearchOrganizationResponse.Status]
        STATUS_ERROR: _ClassVar[SearchOrganizationResponse.Status]
        STATUS_INVALID_ACCEPTOR_ID: _ClassVar[SearchOrganizationResponse.Status]
    STATUS_UNSPECIFIED: SearchOrganizationResponse.Status
    STATUS_SUCCESS: SearchOrganizationResponse.Status
    STATUS_ERROR: SearchOrganizationResponse.Status
    STATUS_INVALID_ACCEPTOR_ID: SearchOrganizationResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    status: SearchOrganizationResponse.Status
    error: _error_pb2.Error
    organizations: _containers.RepeatedCompositeFieldContainer[Organization]
    def __init__(self, status: _Optional[_Union[SearchOrganizationResponse.Status, str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., organizations: _Optional[_Iterable[_Union[Organization, _Mapping]]] = ...) -> None: ...
