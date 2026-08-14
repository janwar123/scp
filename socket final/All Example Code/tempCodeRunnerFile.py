import socket

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(("localhost",5000))

server.listen(1)

print("Waiting for client...")

client,address = server.accept()

client.send(
"Welcome to TCP Socket".encode()
)

client.close()

server.close()