import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost",5000))

print("Waiting...")

data,address = server.recvfrom(1024)

print("Client:",data.decode())

reply = "Welcome to Socket Programming"

server.sendto(reply.encode(),address)

server.close()