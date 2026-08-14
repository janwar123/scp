import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

filename = input("Enter file name: ")

client.send(filename.encode())

newfile = open("downloaded_" + filename, "wb")

while True:

    data = client.recv(1000)

    if not data:
        break

    newfile.write(data)

newfile.close()

client.close()

print("Download Complete")