import pytest
import grpc

from concurrent import futures
from sdk import build_partner_client
from sdk.mica.partner.service.v1.partner_to_mica_service_pb2_grpc import PartnerToMicaService, \
    add_PartnerToMicaServiceServicer_to_server
import sdk.mica.member.ping.v1.ping_service_pb2 as ping


def test_partner_client():
    addr='[::]:50051'
    server = build_partner_grpc_server(addr=addr)
    server.start()
    insecure_channel = grpc.insecure_channel(addr)
    partner_client = build_partner_client(insecure_channel)
    assert partner_client is not None
    ping_response = partner_client.Ping(ping.PingRequest())
    server.stop(grace=None)
    server.wait_for_termination()
    assert ping_response is not None
    assert ping_response.status == ping.PingResponse.STATUS_SUCCESS
    assert ping_response.build_version == 'test version'
    assert ping_response.server_time is not None


class MockToMicaPartnerServicer(PartnerToMicaService):

    def Ping(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        response = ping.PingResponse(status=ping.PingResponse.STATUS_SUCCESS, build_version='test version')
        response.server_time.GetCurrentTime()
        return response


def build_partner_grpc_server(addr: str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PartnerToMicaServiceServicer_to_server(MockToMicaPartnerServicer(), server)
    server.add_insecure_port(addr)
    return server
