import socket

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

file = open("received_udp.txt", "w")

while True:
    data, addr = server.recvfrom(1024)
    text = data.decode()
    
    if text == "END":
        break
        
    file.write(text)

file.close()
server.close()