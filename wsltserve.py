import asyncio
import ssl
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("/etc/letsencrypt/live/njfev2.buzz/fullchain.pem", "/etc/letsencrypt/live/njfev2.buzz/privkey.pem")

start_server = websockets.serve(
    hello, '127.0.0.1', 443, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



