# Copyright 2015, Google Inc.
# All rights reserved.
# ...

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
from build import hello_pb2
from build import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()