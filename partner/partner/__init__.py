import grpc

from partner.mica.partner.service.v1.partner_to_mica_service_pb2_grpc import PartnerToMicaServiceStub
from micautils import create_test_channel, create_test_jwt_token

partner_roles = ['RolePartnerAdmin']

def build_test_partner_client(tenant: str, addr: str = '[::]:50051'):
    subject = tenant
    audience = 'partner.mica.io'
    claims = {"tenant": tenant}
    channel = create_test_channel(addr=addr, jwt_subject=subject, jwt_audience=audience, jwt_roles=partner_roles,
                                  jwt_claims=claims)
    return build_partner_client(channel=channel)

def build_partner_client(channel: grpc.Channel):
    stub = PartnerToMicaServiceStub(channel)
    return stub


def build_partner_client(channel: grpc.Channel):
    stub = PartnerToMicaServiceStub(channel=channel)
    return stub
