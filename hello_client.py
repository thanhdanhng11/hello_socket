import socket

# 1. create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect to server
client_socket.connect(("localhost", 12345))

# 3. receive data from server
data = client_socket.recv(1024) # maximum is 1024 bytes
print("Recieve data from server: ", data.decode())

# 4. disconnect
client_socket.close()