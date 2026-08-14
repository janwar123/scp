import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter Message: ")

client.sendto(message.encode(), ("localhost", 5000))

print("Message Sent Successfully")

client.close()