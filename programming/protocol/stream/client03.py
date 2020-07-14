#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import grpc
import Queue
import schema_pb2
import schema_pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = schema_pb2_grpc.GatewayStub(channel)
        while True:
            queue = Queue.Queue()
            queue.put(1)
            try:
                resp = stub.Call(generate_message(queue))
                for r in resp:
                    num = r.num
                    queue.put(num)
            except grpc.RpcError as e:
                print "stream call err, code: %s, msg: %s" % (e.code(), e.details())
            except Exception as e:
                print "unknown err:", e
            finally:
                queue.put("exit")
                time.sleep(1)


def generate_message(queue):
    while True:
        num = queue.get()
        if num == "exit":
            return
        print num
        yield schema_pb2.Request(num=num)


if __name__ == "__main__":
    main()