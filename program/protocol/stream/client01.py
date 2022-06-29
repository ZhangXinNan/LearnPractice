#!/usr/bin/env python
# -*- coding: utf-8 -*-


import grpc

import schema_pb2
import schema_pb2_grpc
# python2
# import Queue
# queue = Queue.Queue()

import queue
queue = queue.Queue()


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = schema_pb2_grpc.GatewayStub(channel)
        queue.put(1)
        resp = stub.Call(generate_message())
        for r in resp:
            num = r.num
            queue.put(num)


def generate_message():
    while True:
        num = queue.get()
        print(num)
        yield schema_pb2.Request(num=num)


if __name__ == "__main__":
    main()