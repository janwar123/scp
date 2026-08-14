import socket

HOST="127.0.0.1"
PORT=5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()

print("Waiting...")

client,address=server.accept()

print("Connected")

while True:

    msg=client.recv(1024).decode()

    print("Client :",msg)

    reply=input("You : ")

    client.send(reply.encode())