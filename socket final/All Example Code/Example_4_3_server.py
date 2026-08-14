import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))

server.listen()

print("Server Started...")

while True:

    client, address = server.accept()

    print("Connected:", address)

    client.send(
        "Welcome".encode()
    )

    client.close()