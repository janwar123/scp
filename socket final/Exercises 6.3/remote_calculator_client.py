import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

num1 = input("Enter First Number : ")

num2 = input("Enter Second Number : ")

op = input("Enter Operator (+ - * / %) : ")

message = num1 + "," + num2 + "," + op

client.send(message.encode())

result = client.recv(1024).decode()

print("\nResult =", result)

client.close()