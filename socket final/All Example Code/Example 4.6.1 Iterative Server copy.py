import socket
import time

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running...")
print("Waiting for clients...\n")

while True:
    client, address = server.accept()
    print(f"Connected: {address}")

    count = int(client.recv(1024).decode())

    total = 0
    for i in range(1, count + 1):
        total += i
        time.sleep(0.2)   # 200 milliseconds delay

    client.send(str(total).encode())

    print(f"Sent Sum = {total}\n")

    client.close()