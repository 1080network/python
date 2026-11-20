from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperatingSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATING_SYSTEM_UNSPECIFIED: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_OTHER: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_ANDROID: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_IOS: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_WINDOWS: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_LINUX: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_MACOS: _ClassVar[OperatingSystem]
    OPERATING_SYSTEM_CHROMEOS: _ClassVar[OperatingSystem]

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TYPE_UNSPECIFIED: _ClassVar[DeviceType]
    DEVICE_TYPE_OTHER: _ClassVar[DeviceType]
    DEVICE_TYPE_TABLET: _ClassVar[DeviceType]
    DEVICE_TYPE_TERMINAL: _ClassVar[DeviceType]
    DEVICE_TYPE_SMARTPHONE: _ClassVar[DeviceType]
    DEVICE_TYPE_COMPUTER: _ClassVar[DeviceType]
    DEVICE_TYPE_WEARABLE: _ClassVar[DeviceType]
    DEVICE_TYPE_BROWSER: _ClassVar[DeviceType]

class AuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHENTICATION_TYPE_UNSPECIFIED: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_OTHER: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_NONE: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_PIN: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_CREDENTIAL: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_BIOMETRIC_WEAK: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_BIOMETRIC_STRONG: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_CERTIFICATE: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_MFA_WEAK: _ClassVar[AuthenticationType]
    AUTHENTICATION_TYPE_MFA_STRONG: _ClassVar[AuthenticationType]

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_TYPE_UNSPECIFIED: _ClassVar[UserType]
    USER_TYPE_OTHER: _ClassVar[UserType]
    USER_TYPE_PERSON: _ClassVar[UserType]
    USER_TYPE_SERVICE_ACCOUNT: _ClassVar[UserType]
OPERATING_SYSTEM_UNSPECIFIED: OperatingSystem
OPERATING_SYSTEM_OTHER: OperatingSystem
OPERATING_SYSTEM_ANDROID: OperatingSystem
OPERATING_SYSTEM_IOS: OperatingSystem
OPERATING_SYSTEM_WINDOWS: OperatingSystem
OPERATING_SYSTEM_LINUX: OperatingSystem
OPERATING_SYSTEM_MACOS: OperatingSystem
OPERATING_SYSTEM_CHROMEOS: OperatingSystem
DEVICE_TYPE_UNSPECIFIED: DeviceType
DEVICE_TYPE_OTHER: DeviceType
DEVICE_TYPE_TABLET: DeviceType
DEVICE_TYPE_TERMINAL: DeviceType
DEVICE_TYPE_SMARTPHONE: DeviceType
DEVICE_TYPE_COMPUTER: DeviceType
DEVICE_TYPE_WEARABLE: DeviceType
DEVICE_TYPE_BROWSER: DeviceType
AUTHENTICATION_TYPE_UNSPECIFIED: AuthenticationType
AUTHENTICATION_TYPE_OTHER: AuthenticationType
AUTHENTICATION_TYPE_NONE: AuthenticationType
AUTHENTICATION_TYPE_PIN: AuthenticationType
AUTHENTICATION_TYPE_CREDENTIAL: AuthenticationType
AUTHENTICATION_TYPE_BIOMETRIC_WEAK: AuthenticationType
AUTHENTICATION_TYPE_BIOMETRIC_STRONG: AuthenticationType
AUTHENTICATION_TYPE_CERTIFICATE: AuthenticationType
AUTHENTICATION_TYPE_MFA_WEAK: AuthenticationType
AUTHENTICATION_TYPE_MFA_STRONG: AuthenticationType
USER_TYPE_UNSPECIFIED: UserType
USER_TYPE_OTHER: UserType
USER_TYPE_PERSON: UserType
USER_TYPE_SERVICE_ACCOUNT: UserType

class DeviceIdentifier(_message.Message):
    __slots__ = ("device_type", "device_os", "device_name", "device_identifier", "device_user_agent", "ip_address")
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_OS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    device_type: DeviceType
    device_os: OperatingSystem
    device_name: str
    device_identifier: str
    device_user_agent: str
    ip_address: str
    def __init__(self, device_type: _Optional[_Union[DeviceType, str]] = ..., device_os: _Optional[_Union[OperatingSystem, str]] = ..., device_name: _Optional[str] = ..., device_identifier: _Optional[str] = ..., device_user_agent: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...

class DeviceUser(_message.Message):
    __slots__ = ("user_type", "user_identifier", "user_authentication")
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    user_type: UserType
    user_identifier: str
    user_authentication: _containers.RepeatedScalarFieldContainer[AuthenticationType]
    def __init__(self, user_type: _Optional[_Union[UserType, str]] = ..., user_identifier: _Optional[str] = ..., user_authentication: _Optional[_Iterable[_Union[AuthenticationType, str]]] = ...) -> None: ...

class Origin(_message.Message):
    __slots__ = ("device_data", "user_data")
    DEVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_FIELD_NUMBER: _ClassVar[int]
    device_data: DeviceIdentifier
    user_data: DeviceUser
    def __init__(self, device_data: _Optional[_Union[DeviceIdentifier, _Mapping]] = ..., user_data: _Optional[_Union[DeviceUser, _Mapping]] = ...) -> None: ...

class RiskSignal(_message.Message):
    __slots__ = ("origins",)
    ORIGINS_FIELD_NUMBER: _ClassVar[int]
    origins: _containers.RepeatedCompositeFieldContainer[Origin]
    def __init__(self, origins: _Optional[_Iterable[_Union[Origin, _Mapping]]] = ...) -> None: ...
