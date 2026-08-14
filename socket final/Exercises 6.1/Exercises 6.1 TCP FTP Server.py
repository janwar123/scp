import socket

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting...")

client, addr = server.accept()

file = open("received.txt", "wb")

while True:

    data = client.recv(100)

    if not data:
        break

    file.write(data)

    client.send(b"ACK")

file.close()

client.close()