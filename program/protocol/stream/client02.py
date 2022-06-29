#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
问题就出在队列 queue 上！

当 server 重启时，client 报错后重新调用 stub.Call() 会新开启一个线程来执行 generate_message()，这时候就会有两个 generate_message() 的线程同时从 queue 中读取数据。而且，第一个线程把数据从 queue 获取后，由于该线程所属的stream连接已经断开了，并不能把数据发送给 server；而第二个线程虽然连接正常，但却阻塞在 queue.get() 。

因此，generate_message() 中也存在线程泄露的问题。如果我们在代码中用 threading.active_count() 将可以看到线程的数量越来越多。
'''

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
        while True:
            try:
                queue.put(1)
                resp = stub.Call(generate_message())
                for r in resp:
                    num = r.num
                    queue.put(num)
            except grpc.RpcError as e:
                print("stream all err, code : {}, msg: {}".format(e.code(), e.details()))
                time.sleep(1)


def generate_message():
    while True:
        num = queue.get()
        print(num)
        yield schema_pb2.Request(num=num)


if __name__ == "__main__":
    main()