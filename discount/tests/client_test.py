from concurrent import futures

import grpc

from micadiscount.discount.service.v1.discount_service_pb2_grpc import add_DiscountServiceServicer_to_server, DiscountService
import micadiscount.common.ping.v1.ping_pb2 as ping
from micadiscount import build_test_discount_client


def test_discount_ping():
    server = get_discount_server()
    server.start()
    client = build_test_discount_client(addr='[::]:50051')
    response = client.Ping(ping.PingRequest())
    assert response.status == ping.PingResponse.STATUS_SUCCESS
    assert response.build_version == 'test version'
    assert response.server_time is not None
    print('status: {0} and build version {1} time: {2}'.format(response.status, response.build_version,
                                                               response.server_time))
    server.stop(grace=None)
    server.wait_for_termination()


def get_discount_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DiscountServiceServicer_to_server(MockMicaDiscount(), server)
    server.add_insecure_port('[::]:50051')
    return server


class MockMicaDiscount(DiscountService):

    def Ping(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        response = ping.PingResponse(status=ping.PingResponse.STATUS_SUCCESS, build_version='test version')
        response.server_time.GetCurrentTime()
        return response
