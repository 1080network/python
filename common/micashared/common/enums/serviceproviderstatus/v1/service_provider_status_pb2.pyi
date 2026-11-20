from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceProviderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_PROVIDER_STATUS_UNSPECIFIED: _ClassVar[ServiceProviderStatus]
    SERVICE_PROVIDER_STATUS_ACTIVE: _ClassVar[ServiceProviderStatus]
    SERVICE_PROVIDER_STATUS_INACTIVE: _ClassVar[ServiceProviderStatus]
SERVICE_PROVIDER_STATUS_UNSPECIFIED: ServiceProviderStatus
SERVICE_PROVIDER_STATUS_ACTIVE: ServiceProviderStatus
SERVICE_PROVIDER_STATUS_INACTIVE: ServiceProviderStatus
