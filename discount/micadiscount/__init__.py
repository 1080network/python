import grpc
from micautils import create_channel

import micadiscount.discount.service.v1.discount_service_pb2_grpc as discount

discount_roles = ['RoleDiscountAdmin']


def build_test_discount_client(addr: str = 'localhost:14100'):
    channel = create_channel(addr=addr, jwt_roles=discount_roles)
    return build_discount_client(channel=channel)


def build_discount_client(channel: grpc.Channel):
    stub = discount.DiscountServiceStub(channel)
    return stub
