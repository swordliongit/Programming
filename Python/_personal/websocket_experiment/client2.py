import asyncio
import websockets
 
async def test(client_id):
    async with websockets.connect('ws://localhost:8000') as websocket:
        # send client identifier to the server
        await websocket.send(client_id)
        response = await websocket.recv()
        print(response)
 
async def run_client(client_id):
    while True:
        await test(client_id)
        await asyncio.sleep(5)
 
asyncio.get_event_loop().run_until_complete(run_client("client2"))