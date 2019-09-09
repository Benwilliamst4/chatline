import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
y = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

x.bind((HOST, PORT))
x.listen()
y.connect((HOST, PORT))
