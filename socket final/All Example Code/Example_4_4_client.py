import socket
import pickle

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect(("localhost",5000))

employee = {
    "id":101,
    "name":"Arman",
    "salary":25000
}

data = pickle.dumps(employee)

client.send(data)

client.close()