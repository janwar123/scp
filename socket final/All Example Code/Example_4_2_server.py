import socket

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(("localhost",5000))

server.listen()

print("Waiting for client...")

client,address = server.accept()

client.send(
"Welcome".encode()
)

reply = client.recv(1024)

print("Client:",reply.decode())

client.close()

server.close()