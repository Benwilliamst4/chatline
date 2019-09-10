"""
Primary use case:
./chatline.py 10.123.345.678

This process starts two threads, a socket attempting to connect on 10.123.345.678
and a socket accepting a connection on 10.123.345.678.

Whichever is hit first will terminate the other thread and become the primary thread.
Port will be 1337 by default - no override.
"""

import threading
import socket
import sys
import time

class Client:
    PORT = 8080

    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, self.PORT))
        self.sock.sendall(bytes(input('enter sheet: '), 'utf-8'))
        x = self.sock.recv(420)
        print(x)
        

class Server:
    PORT = 8080
    HOST = '127.0.0.1'

    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)
        conn, ip = self.sock.accept()
        with conn:
            string = conn.recv(420)
            print(string)
            conn.sendall(bytes(input('enter sheet: '), 'utf-8'))


if __name__ == '__main__':
    if sys.argv[1] == 'client':
        x = Client('127.0.0.1')
    else:
        x = Server('127.0.0.1')
