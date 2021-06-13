import asyncio
import websockets

class MessageType:
    DISCONNECT = "DISCONNECT"
    LETTER     = "LETTER"

class Client:

    instance = None

    def __init__(self, connection_string):
        
        if Client.instance == None:
            Client.instance = self

        self.connection_string = connection_string
        self.clientsock = None


    async def start_client(self):
        self.clientsock = await websockets.connect(self.connection_string)
        while True:
            inp = input("enter message")
            await self.send_letter(inp)

    async def send_message(self, msg_type, msg):
        packet = Client.pack_message(msg_type, msg)
        await self.clientsock.send(packet)
        
    async def send_letter(self, letter):
        assert len(letter) == 1, "Send letter should be sending a single letter"

        await self.send_message(MessageType.LETTER, letter)

    def unpack_message(self, packet):
        msg_type, msg = packet.split('$', 1)
        if msg_type == MessageType.MESSAGE:
            pass
        else: pass

    @staticmethod
    def pack_message(msg_type, msg):
        return f"{msg_type}${msg}"

if __name__ == "__main__":
    morse_client = Client(f"ws://{IP}:{PORT}")

