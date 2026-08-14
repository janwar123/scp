import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", 5000))

print("Receiver is waiting...")

data, address = server.recvfrom(1024)

print("Message:", data.decode())

print("Sender Address:", address)

server.close()