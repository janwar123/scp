import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.settimeout(2.0) 

file = open("sample.txt", "rb")

while True:
    chunk = file.read(100)
    if not chunk:
        break

    ack_received = False
    while not ack_received:
        try:
            client.send(chunk)
            
            ack = client.recv(1024)
            if ack == b"ACK":
                print("ACK received for chunk!")
                ack_received = True 
                
        except socket.timeout:
            print("Timeout! Resending chunk...")

file.close()
client.close()