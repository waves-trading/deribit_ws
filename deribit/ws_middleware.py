import json
import ssl

import websockets as websockets
from ccxt.async_support import Exchange


class WSExchange(Exchange):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ws_descriptor = None
        self.ws_message_counter = 0

    async def __aenter__(self):
        if not self.ws_url:
            raise Exception()
        conn = websockets.connect(self.ws_url, ssl=ssl.SSLContext())
        return conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type)
            print(exc_val)
            print(str(exc_tb))
        else:
            await self.close()

    async def fetch(self, url, method='', headers=None, body=None):
        request_message = {
            "jsonrpc": "2.0",
            "method": f"{method}/{url}",
            "params": body
        }
        self.ws_message_counter += 1
        response = await self._fetch_ws(
                request_message
            )
        # print(response)
        response = json.loads(response)
        # self.handle_errors(None, None, url, method, None, body, response, None, body)
        return response

    async def _fetch_ws(self, req):
        await self.ws_descriptor.send(json.dumps(req))
        response = await self.ws_descriptor.recv()
        return response

    def login_ws(self, *args, **kwargs):
        raise NotImplementedError
