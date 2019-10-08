#!/usr/bin/env python3

from server import Server
from client import send
from _thread import *
import threading, time

LOCAL_HOST = "0.0.0.0"
PORT = 60777


def start_server():
    server = Server(LOCAL_HOST, PORT)


def main():
    start_new_thread(start_server, ())

    while True and threading.main_thread():
        select = input('Choose to (m)essage, (q)uit: ')

        # Used to indicate whether the communication is local or not
        local_flag = False

        # Quit
        if select is 'q':
            break

        # Message
        if select is 'm':
            address = input('Enter target IP address: ')

            if address is LOCAL_HOST or "127.0.0.1":
                local_flag = True

            message = input('Enter a message to send: ')

            send(address, PORT, message)

        if local_flag:
            time.sleep(.1)


if __name__ == '__main__':
    main()
