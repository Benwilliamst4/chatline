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

class ThreadController:

    client = False
    server = False

    def __init__(self, ip):
        self.is_valid_ipv4(ip)
        self.start_threads()
    
    def is_valid_ipv4(self, ip):
        self.ip = ip
        socket.inet_pton(socket.AF_INET, self.ip)

    def start_threads(self):
        t1 = ClientServerThread(target = init_client_thread, args =(lambda : self.client, self.ip)) 
        t1.start() 
        t2 = ClientServerThread(target = init_server_thread, args =(lambda : self.server, self.ip)) 
        t2.start() 
        while (True):
            if self.client:
                print('Client Wins')
                return
            if self.server:
                print('Server Wins')
                return


class ClientServerThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(ClientServerThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

if __name__ == '__main__':
    controller_singleton = ThreadController(sys.argv[1])
