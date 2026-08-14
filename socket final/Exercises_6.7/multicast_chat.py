import socket
import struct
import threading


MULTICAST_GROUP = "224.1.1.1"
PORT = 5000



def receive_messages(sock):

    while True:

        data, address = sock.recvfrom(1024)

        print(f"\n{address}: {data.decode()}")
        print("You: ", end="", flush=True)


def send_messages(sock):

    while True:

        message = input("You: ")

        sock.sendto(
            message.encode(),
            (MULTICAST_GROUP, PORT)
        )


sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("", PORT))


group = socket.inet_aton(MULTICAST_GROUP)

membership = struct.pack(
    "4sL",
    group,
    socket.INADDR_ANY
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    membership
)

print("Joined multicast group.")
print("Start chatting...\n")


receive_thread = threading.Thread(
    target=receive_messages,
    args=(sock,),
    daemon=True
)

receive_thread.start()


try:

    send_messages(sock)

except KeyboardInterrupt:

    print("\nChat closed.")

    sock.close()