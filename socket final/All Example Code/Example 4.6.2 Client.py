import socket

HOST = "127.0.0.1"
PORT = 5000

count = int(input("Enter Count: "))

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send(str(count).encode())

print("Sum =",
      client.recv(1024).decode())

client.close()