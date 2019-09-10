import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080     # The port used by the server

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
y = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

x.bind((HOST, PORT))

