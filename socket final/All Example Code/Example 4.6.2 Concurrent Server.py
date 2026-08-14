import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Concurrent Server Started...")


def handle_client(client):
    count = int(client.recv(1024).decode())

    total = 0

    for i in range(1, count + 1):
        total += i
        time.sleep(0.2)

    client.send(str(total).encode())

    client.close()


while True:
    client, address = server.accept()

    print("Connected:", address)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()