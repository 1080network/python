import grpc

import micadiscount.discount.service.v1.discount_service_pb2_grpc as discount


class CertLoader:
    root_certificates = None
    private_key = None
    certificate_chain = None

    def __init__(self, root_certificate_pem_file: str = None, root_certificate_bytes: bytes = None,
                 private_key_pem_file: str = None, private_key_bytes: bytes = None):
        if root_certificate_pem_file is not None:
            self.root_certificates = open(root_certificate_pem_file, 'rb').read()
        else:
            self.root_certificates = root_certificate_bytes
        if private_key_pem_file is not None:
            self.private_key


def create_channel(addr: str, credentials: grpc.ChannelCredentials = None, certificates: CertLoader = None,
                   options=None, compression=None):
    if certificates is None and credentials is None:
        return grpc.insecure_channel(addr, options, compression)
    else:
        if credentials is None:
            credentials = grpc.ssl_channel_credentials(root_certificates=certificates.root_certificates,
                                                       private_key=certificates.private_key,
                                                       certificate_chain=certificates.certificate_chain)
        return grpc.secure_channel(target=addr,
                                   credentials=credentials,
                                   options=options,
                                   compression=compression
                                   )


def build_discount_client(channel: grpc.Channel):
    stub = discount.DiscountServiceStub(channel)
    return stub
