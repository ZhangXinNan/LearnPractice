#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grpc
import time
import schema_pb2
import schema_pb2_grpc
from concurrent import futures


class GatewayServer(schema_pb2_grpc.GatewayServicer):

    def Call(self, request_iterator, context):
        for req in request_iterator:
            yield schema_pb2.Response(num=req.num+1)
            time.sleep(1)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_GatewayServicer_to_server(GatewayServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
