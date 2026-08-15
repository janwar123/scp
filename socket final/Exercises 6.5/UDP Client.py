import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    try:

        message = input("Client: ")

        client.sendto(message.encode(), (HOST, PORT))

        reply, addr = client.recvfrom(1000)

        print("Server:", reply.decode())

    except KeyboardInterrupt:
        print("\nClient Closed")
        break

client.close()
