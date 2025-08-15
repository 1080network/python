from concurrent import futures

import grpc
import pytest
from protoc_gen_validate.validator import validate, ValidationFailed

from discount.mica.discount.service.v1.discount_to_mica_service_pb2_grpc import add_DiscountToMicaServiceServicer_to_server, DiscountToMicaService
import discount.mica.member.ping.v1.ping_service_pb2 as ping
import discount.mica.discount.discount.v1.discount_pb2 as discount_pb
from discount import build_test_discount_client, get_test_jwt_token


def test_discount_ping():
    server = get_discount_server()
    server.start()
    client = build_test_discount_client(tenant='micatenant', addr='[::]:50051')
    response = client.Ping(ping.PingRequest())
    assert response.status == ping.PingResponse.STATUS_SUCCESS
    assert response.build_version == 'test version'
    assert response.server_time is not None
    print('status: {0} and build version {1} time: {2}'.format(response.status, response.build_version,
                                                               response.server_time))
    server.stop(grace=None)
    server.wait_for_termination()


def test_validate_usage():
    discount = discount_pb.Discount(discount_definition_key='lessthanexpected')
    with pytest.raises(ValidationFailed) as e_info:
        validate(discount)


def test_create_token():
    token = get_test_jwt_token(tenant='micatenant')
    print(f"Your calling token is: \n {token}")


def get_discount_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DiscountToMicaServiceServicer_to_server(MockMicaDiscount(), server)
    server.add_insecure_port('[::]:50051')
    return server


class MockMicaDiscount(DiscountToMicaService):

    def Ping(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        response = ping.PingResponse(status=ping.PingResponse.STATUS_SUCCESS, build_version='test version')
        response.server_time.GetCurrentTime()
        return response
