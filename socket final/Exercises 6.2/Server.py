import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 5000


def send_file(client):

    filename = client.recv(1024).decode()

    try:
        file = open(filename, "rb")

        while True:

            data = file.read(1000)

            if not data:
                break

            client.send(data)

            time.sleep(0.2)

        file.close()

    except:

        client.send(b"File Not Found")

    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server Running...")


while True:

    client, addr = server.accept()

    print("Connected:", addr)

    thread = threading.Thread(target=send_file, args=(client,))

    thread.start()