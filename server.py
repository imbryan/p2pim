#!/usr/bin/env python3

import sys, socket
from _thread import *
import threading


class Server:
    def interpret(self, message, address):
        print('{} says: {}'.format(address, message.decode()))

    def child_thread(self, conn, lock, address):
        try:
            buffer = b''

            while True:
                conn.settimeout(10)
                data = conn.recv(1024)

                if not data:
                    lock.release()
                    break

                buffer += data

            self.interpret(buffer, address)

        except Exception as e:
            sys.stderr.write('Error: {}'.format(e))

        conn.close()

    def __init__(self, address, port):
        lock = threading.Lock()

        # Create the server socket
        server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Binding and listening
        try:
            server_sock.bind((address, port))
            server_sock.listen()
        except Exception as e:
            sys.stderr.write('Error: {}'.format(e))
            sys.exit(1)

        while True:
            conn, addr = server_sock.accept()

            lock.acquire()

            start_new_thread(self.child_thread, (conn, lock, addr[0]))

