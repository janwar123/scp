import socket
import pickle

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(("localhost",5000))

server.listen()

client,address = server.accept()

data = client.recv(1024)

employee = pickle.loads(data)

print(employee["id"])
print(employee["name"])
print(employee["salary"])

client.close()

server.close()