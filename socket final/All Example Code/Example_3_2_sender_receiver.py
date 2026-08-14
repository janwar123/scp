import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = "Trying to Connect"

client.sendto(message.encode(),
              ("localhost",5000))

data,address = client.recvfrom(1024)

print(data.decode())

client.close()