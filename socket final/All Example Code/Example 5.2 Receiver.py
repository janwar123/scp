import socket
import struct

GROUP = "224.0.0.1"
PORT = 3456

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind(("", PORT))

mreq = struct.pack(
    "4sl",
    socket.inet_aton(GROUP),
    socket.INADDR_ANY
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

print("Waiting...")

data, addr = sock.recvfrom(1024)

print("Received:", data.decode())