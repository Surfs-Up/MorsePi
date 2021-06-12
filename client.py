import socket
import threading

PACKETSIZE = 64
# SERVER = "192.168.1.55"
SERVER = "127.0.0.1"
PORT = 5050
FORMAT = 'utf-8'

class MessageType:
    DISCONNECT = "DISCONNECT"
    LETTER     = "LETTER"

class Client:

    clientsock = None

    def __init__(self, server, port):
        self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsock.connect((server, port))

    def send_message(self, msg_type, msg):
        packet = Client.pack_message(msg_type, msg).encode(FORMAT)
        packet += b' '*(PACKETSIZE-len(packet))
        self.clientsock.send(packet)

    def send_letter(self, letter):
        assert len(letter) == 1, "Send letter should be sending a single letter"

        self.send_message(MessageType.LETTER, letter)

    @staticmethod
    def pack_message(msg_type, msg):
        return f"{msg_type}${msg}"

client = Client(SERVER, PORT)
client.send_letter("i")

