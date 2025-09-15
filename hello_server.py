import socket

# 1. create socket (AF_INET = IPv4, SOCK_STEAM = TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. bind it into the address and gate
server_socket.bind(("localhost", 12345))

# 3. allow listen connects
server_socket.listen(1) # 1 = the maximum of client
print("Server is connecting, waiting to connect...")

# 4. accept the connection
conn, addr = server_socket.accept()
print(f"Connect from {addr}")

# 5. send the data
message = "Hello, Client!"
conn.sendall(message.encode())

# 6. disconnect
conn.close()
server_socket.close()