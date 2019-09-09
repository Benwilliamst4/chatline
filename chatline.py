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

claimed_client = False
claimed_server = False

class ThreadStarter:

    def __init__(self, ip):
        self.is_valid_ipv4(ip)
        self.start_threads()
    
    def is_valid_ipv4(self, ip):
        self.ip = ip
        socket.inet_pton(socket.AF_INET, self.ip)

    def start_threads(self):
        threads = []
        t1 = threading.Thread(name='client', target = init_client_thread), args=(self.ip,)) 
        t1.start() 
        threads.append(t1)
        t2 = threading.Thread(name='server', target = init_server_thread, arg-=(self.ip,)) 
        t2.start() 
        threads.append(t2)
        for i in threads:
            print(i)

class ServerSocket():

    def __init__(self, ip):
        pass


class ClientSocket()

    def __init__(self, ip):
        pass


def init_client_thread():
    global claimed_server
    global claimed_client
    while (not claimed_server):
        time.sleep(1)
    print('client')
    pass

def init_server_thread():
    global claimed_client
    global claimed_server
    while (not claimed_client):
        time.sleep(1)
        claimed_server = True
    print('server')
    pass


if __name__ == '__main__':
    controller_singleton = ThreadStarter(sys.argv[1])
