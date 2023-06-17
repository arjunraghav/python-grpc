from __future__ import print_function

import logging

import grpc
import users_pb2
import users_pb2_grpc


def run():
    response = []
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())
    print(response.users)


if __name__ == "__main__":
    logging.basicConfig()
    run()