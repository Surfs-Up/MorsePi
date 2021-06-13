
import asyncio

from morsesend import MorseEncoder
from client import Client

IP = "192.168.1.55"
PORT = 5050

morse_client = Client(f"ws://{IP}:{PORT}")
encoder = MorseEncoder()      

loop = asyncio.get_event_loop()
# loop.run_until_complete(morse_client.start_client())
asyncio.ensure_future(morse_client.start_client())
asyncio.ensure_future(encoder.run())
loop.run_forever()
