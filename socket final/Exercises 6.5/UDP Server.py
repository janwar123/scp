import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Server Started")

while True:

    try:

        message, client_address = server.recvfrom(1000)

        print("\nClient:", message.decode())

        reply = input("Server: ")

        server.sendto(reply.encode(), client_address)

    except KeyboardInterrupt:
        print("\nServer Closed")
        break

server.close()
