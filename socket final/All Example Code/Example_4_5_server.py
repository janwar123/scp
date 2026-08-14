import socket

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(("localhost",5000))

server.listen()

client,address = server.accept()

file = client.makefile()

num1 = int(file.readline())

num2 = int(file.readline())

print(num1 + num2)

client.close()

server.close()