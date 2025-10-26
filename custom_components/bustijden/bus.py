import aiohttp
from .const import API_URL
import base64


class Bus:
    def __init__(self, base_key, amount):
        self.base_key = base_key
        self.amount = amount
        self.stop_name = self.base64_decode()

    def base64_decode(self):
        try:
            decoded_bytes = base64.b64decode(self.base_key)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    async def get_next_buses(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_URL}/stops/{self.base_key}") as response:
                data = await response.json()
                stopTimes = list(data)[:self.amount]
                return stopTimes
