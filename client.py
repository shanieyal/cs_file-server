import socket

my_socket = socket.socket()
my_socket.connect(('127.0.0.1',8820))
my_socket.send('hello')
data = my_socket.recv(1024)
print data
my_socket.close()