import grpc
from micautils import create_channel

import mica.connect.service.v1.connect_service_pb2_grpc as connect

connect_roles = ['RoleConnectAdmin']


def build_test_connect_client(addr: str = '[::]:13700'):
    channel = create_channel(addr=addr, jwt_roles=connect_roles)
    return build_connect_client(channel=channel)


def build_connect_client(channel: grpc.Channel):
    stub = connect.ConnectServiceStub(channel=channel)
    return stub
