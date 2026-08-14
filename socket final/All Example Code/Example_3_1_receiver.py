import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", 5000))

print("Waiting for message...")

data, address = server.recvfrom(40)

print("Received:", data.decode())

server.close()