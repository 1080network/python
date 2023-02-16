import grpc
from micautils import create_channel

import serviceprovider.mica.serviceprovider.service.v1.service_provider_to_mica_service_pb2_grpc as serviceprovider

partner_roles = ['RoleServiceProviderAdmin']


def build_test_serviceprovider_client(addr: str = '[::]:13400'):
    channel = create_channel(addr=addr, jwt_roles=partner_roles)
    return build_serviceprovider_client(channel=channel)


def build_serviceprovider_client(channel: grpc.Channel):
    stub = serviceprovider.ServiceProviderToMicaServiceStub(channel=channel)
    return stub
