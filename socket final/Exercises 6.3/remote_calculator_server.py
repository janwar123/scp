import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server is Running...")

client, addr = server.accept()

print("Connected:", addr)

data = client.recv(1024).decode()

num1, num2, op = data.split(",")

num1 = int(num1)
num2 = int(num2)

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by Zero"

elif op == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Division by Zero"

else:
    result = "Invalid Operator"

client.send(str(result).encode())

client.close()

server.close()