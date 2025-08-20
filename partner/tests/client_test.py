from concurrent import futures

import grpc

from partner.mica.partner.service.v1.partner_to_mica_service_pb2_grpc import PartnerToMicaService, add_PartnerToMicaServiceServicer_to_server
import partner.mica.member.ping.v1.ping_service_pb2 as ping
from partner import create_test_channel, build_test_partner_client


def test_discount_ping():
    server = get_partner_server()
    server.start()
    client = build_test_partner_client(tenant='micatenant', addr='[::]:50051')
    response = client.Ping(ping.PingRequest())
    assert response.status == ping.PingResponse.STATUS_SUCCESS
    assert response.build_version == 'test version'
    assert response.server_time is not None
    print('status: {0} and build version {1} time: {2}'.format(response.status, response.build_version,
                                                               response.server_time))
    server.stop(grace=None)
    server.wait_for_termination()


def get_partner_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PartnerToMicaServiceServicer_to_server(MockMicaPartner(), server)
    server.add_insecure_port('[::]:50051')
    return server


class MockMicaPartner(PartnerToMicaService):

    def Ping(self, request, context):
        response = ping.PingResponse(status=ping.PingResponse.STATUS_SUCCESS, build_version='test version')
        response.server_time.GetCurrentTime()
        return response
