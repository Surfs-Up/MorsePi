
import asyncio

#from morsesend import MorseEncoder
from client import Client

IP = "localhost"
PORT = 5050

morse_client = Client(f"ws://{IP}:{PORT}")

# encoder = MorseEncoder()      
asyncio.get_event_loop().run_until_complete(morse_client.start_client())
