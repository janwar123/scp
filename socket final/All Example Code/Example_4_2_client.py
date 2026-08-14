import socket

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect(("localhost",5000))

message = client.recv(1024)

print("Server:", message.decode())



client.send("Received your message. Thanks".encode())


client.close()