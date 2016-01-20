import socket
import threading

def handle_client():
    # accept a client and handling it
    (client_socket, client_address) = my_socket.accept()
    data = client_socket.recv(1024)
    client_socket.send('hello2')
    print data
    client_socket.close()

my_socket = socket.socket()
my_socket.bind(('0.0.0.0',8820))

for j in range(3):
    my_socket.listen(1)


threads = []
for i in range(5):
    t = threading.Thread(target=handle_client())
    threads.append(t)
    t.start()


