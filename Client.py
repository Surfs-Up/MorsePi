import socket
import threading

PACKETSIZE = 64
# SERVER = "192.168.1.55"
SERVER = "127.0.0.1"
PORT = 5050
FORMAT = 'utf-8'

class Client:

    clientsock = None

    def __init__(self, server, port):
        self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsock.connect((server, port))

    def pack_message(self, msg_type, msg):
        pass

    def send_message(self, msg):
        message = msg.encode(FORMAT)
        length_header = str(len(message)).encode(FORMAT)
        length_header += length_header + b' '*(PACKETSIZE-len(length_header))
        self.clientsock.send(length_header)
        self.clientsock.send(message)

client = Client(SERVER, PORT)
# send_message("i eat poo")

