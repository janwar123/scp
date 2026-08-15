import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print("Server waiting...")

conn, addr = server.accept()

print("Connected:", addr)

while True:
    try:
        message = conn.recv(1024).decode()

        if not message:
            break

        print("\nClient:", message)

        reply = input("Server: ")

        conn.send(reply.encode())

    except KeyboardInterrupt:
        print("\nServer Closed")
        break

conn.close()
server.close()
