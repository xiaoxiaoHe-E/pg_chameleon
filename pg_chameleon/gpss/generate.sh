python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. gpss.proto
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. data.proto