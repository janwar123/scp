import socket

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect(("localhost",5000))

client.send("2\n".encode())

client.send("3\n".encode())

client.close()