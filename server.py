import socket

my_socket = socket.socket()
my_socket.bind(('0.0.0.0',8820))
my_socket.listen(1)
(client_socket, client_address) = my_socket.accept()
data= client_socket.recv(1024)
client_socket.send('hello2')
print data
client_socket.close()
