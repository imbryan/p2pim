#!/usr/bin/env python3

from server import Server
from client import send
from _thread import *
import threading, time

LOCAL_HOST = "127.0.0.1"
PORT = 60777


def start_server():
    server = Server(LOCAL_HOST, PORT)


def main():
    start_new_thread(start_server, ())

    while True and threading.main_thread():
        select = input('Choose to (m)essage, (q)uit: ')

        # Quit
        if select is 'q':
            break

        # Message
        if select is 'm':
            address = input('Enter target IP address: ')

            message = input('Enter a message to send: ')

            send(address, PORT, message)

        time.sleep(.3)


if __name__ == '__main__':
    main()
