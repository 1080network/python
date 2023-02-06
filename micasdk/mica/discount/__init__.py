import grpc

from mica.discount.service.v1.discount_service_test_support_pb2_grpc import DiscountTestSupportServiceStub
from mica.discount.service.v1.discount_to_mica_service_pb2_grpc import DiscountToMicaServiceStub
from micautils import create_test_channel, create_test_jwt_token


discount_roles = ['RoleDiscountExternalServiceAccount', 'AclCanDetermineDiscount']


def get_test_jwt_token(tenant: str):
    return create_test_jwt_token(subject=tenant, audience='discount.mica.io', jwt_roles=discount_roles,
                          extra_claims={"tenant": tenant})


def build_test_discount_client(tenant: str, addr: str = 'localhost:14100'):
    subject = tenant
    audience = 'discount.mica.io'
    claims = {"tenant": tenant}
    channel = create_test_channel(addr=addr, jwt_subject=subject, jwt_audience=audience, jwt_roles=discount_roles,
                                  jwt_claims=claims)
    return build_discount_client(channel=channel)


def build_discount_client(channel: grpc.Channel):
    stub = DiscountToMicaServiceStub(channel)
    return stub


def build_test_discount_test_support_client(tenant: str, addr: str = 'localhost:14100'):
    subject = tenant
    audience = 'discount.mica.io'
    claims = {"tenant": tenant}
    channel = create_test_channel(addr=addr, jwt_subject=subject, jwt_audience=audience, jwt_roles=discount_roles,
                                  jwt_claims=claims)
    return build_discount_test_support_client(channel=channel)


def build_discount_test_support_client(channel: grpc.Channel):
    stub = DiscountTestSupportServiceStub(channel=channel)
    return stub
