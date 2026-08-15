import socket
#struct use to format binary data
import struct
import threading

GROUP = "224.1.1.1"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("", PORT))


group = socket.inet_aton(GROUP)

mreq = struct.pack("4sL", group, socket.INADDR_ANY)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)


def receive():

    while True:

        data, address = sock.recvfrom(1024)

        print("\nReceived:", data.decode())


thread = threading.Thread(target=receive)

thread.daemon = True

thread.start()


while True:

    message = input("You: ")

    sock.sendto(
        message.encode(),
        (GROUP, PORT)
    )
