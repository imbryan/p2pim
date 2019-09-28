#!/usr/bin/env python3

import sys, socket


def send(address, port, message):

    # Create socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    try:
        client_socket.settimeout(10)
        client_socket.connect((address, port))

        # Send message
        client_socket.send(message.encode())

    except Exception as e:
        sys.stderr.write("Error: {}".format(e))

    client_socket.close()


