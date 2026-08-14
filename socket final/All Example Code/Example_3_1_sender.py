import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")

client.sendto(message.encode(), ("localhost", 5000))

print("Message Sent")

client.close()