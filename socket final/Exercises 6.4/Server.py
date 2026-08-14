import socket
import random

HOST="127.0.0.1"
PORT=5000

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind((HOST,PORT))

print("Streaming Server Running")

filename,address=server.recvfrom(1024)

filename=filename.decode()

file=open(filename,"rb")

while True:

    size=random.randint(1000,2000)

    data=file.read(size)

    if not data:

        server.sendto(b"END",address)

        break

    server.sendto(data,address)

file.close()