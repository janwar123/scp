import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def chat(client):

    while True:

        try:

            msg = client.recv(1024).decode()

            if not msg:
                break

            print("\nClient :", msg)

            reply = input("Reply : ")

            client.send(reply.encode())

        except:

            break

    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server Running...")

while True:

    client, addr = server.accept()

    print("Connected :", addr)

    thread = threading.Thread(target=chat, args=(client,))

    thread.start()