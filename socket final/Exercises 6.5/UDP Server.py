import socket

HOST="127.0.0.1"
PORT=5000

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind((HOST,PORT))

print("UDP Chat Server Running")

while True:

    data,address=server.recvfrom(1000)

    print("Client :",data.decode())

    reply=input("You : ")

    server.sendto(reply.encode(),address)