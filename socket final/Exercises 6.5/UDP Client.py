import socket

HOST="127.0.0.1"
PORT=5000

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:

    msg=input("You : ")

    client.sendto(msg.encode(),(HOST,PORT))

    reply,address=client.recvfrom(1000)

    print("Server :",reply.decode())