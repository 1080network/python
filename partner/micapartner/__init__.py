import grpc
from micautils import create_channel

import micapartner.partner.service.v1.partner_to_mica_service_pb2_grpc as partner

partner_roles = ['RolePartnerAdmin']


def build_test_partner_client(addr: str = '[::]:13400'):
    channel = create_channel(addr=addr, jwt_roles=partner_roles)
    return build_partner_client(channel=channel)


def build_partner_client(channel: grpc.Channel):
    stub = partner.PartnerToMicaServiceStub(channel=channel)
    return stub
