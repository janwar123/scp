import socket

HOST="127.0.0.1"
PORT=5000

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

filename=input("Enter filename : ")

client.sendto(filename.encode(),(HOST,PORT))

file=open("received.mp4","wb")

while True:

    data,address=client.recvfrom(2048)

    if data==b"END":

        break

    file.write(data)

file.close()

print("Download Complete")