import socket
import time

HOST = "127.0.0.1"
PORT = 5000

count = int(input("Enter a number: "))

start = time.time()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(str(count).encode())

result = client.recv(1024).decode()

end = time.time()

print("Sum =", result)
print("Time Taken = {:.2f} seconds".format(end - start))

client.close()