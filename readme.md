packages

grpc
grpc-tools

create
.proto file

command to create proto files
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/users.proto
