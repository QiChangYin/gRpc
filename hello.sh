#!/bin/bash
rm -rf build
mkdir build
touch ./build/__init__.py
python -m grpc_tools.protoc -I./protos --python_out=./build --grpc_python_out=./build ./protos/hello.proto
