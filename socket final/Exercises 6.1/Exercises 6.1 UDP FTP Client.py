import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

file = open("sample.txt", "r")

for line in file:
    client.sendto(line.encode(), (HOST, PORT))

client.sendto("END".encode(), (HOST, PORT))

file.close()
client.close()