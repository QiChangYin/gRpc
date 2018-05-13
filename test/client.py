#!/usr/bin/python

import grpc
import time

from build import demo_pb2
from build import demo_pb2_grpc

channel = grpc.insecure_channel('localhost:8080')
stub = demo_pb2_grpc.CalculatorServiceStub(channel)
req = demo_pb2.SquareREQ(number=1000,name="YinQiChang")
response = stub.SquareReq(req)
print response.number

time.sleep(5)