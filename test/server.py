#!/usr/bin/python

import grpc
from concurrent import futures
import time

from build import demo_pb2
from build import demo_pb2_grpc

import cal


class CalService(demo_pb2_grpc.CalculatorServiceServicer):
    def SquareReq(self, request, response):
        response = demo_pb2.SquareREQ()
        response.number = cal.square_request(request.number)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

demo_pb2_grpc.add_CalculatorServiceServicer_to_server(CalService(), server)

print ("Starting server. Listening on port 8080")
server.add_insecure_port('[::]:8080')
server.start()


try:
    while True:
        time.sleep(80000)
except KeyboardInterrupt:
    server.stop(0)