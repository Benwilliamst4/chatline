"""
Primary use case:
./chatline.py 10.123.345.678

This process starts two threads, a socket attempting to connect on 10.123.345.678
and a socket accepting a connection on 10.123.345.678.

Whichever is hit first will terminate the other thread and become the primary thread.
"""

import threading
import socket
import sys

class ThreadController:

    def __init__(self, ip):
        self.ip = ip
        self.is_valid_ipv4()
    
    def is_valid_ipv4(self):
        socket.inet_pton(socket.AF_INET, self.ip)


    


if __name__ == '__main__':
    controller_singleton = ThreadController(sys.argv[1])


