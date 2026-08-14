import socket

MULTICAST_GROUP = "224.0.0.1"
PORT = 3456

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

message = "Hello Everyone"

sock.sendto(message.encode(),
            (MULTICAST_GROUP, PORT))

sock.close()