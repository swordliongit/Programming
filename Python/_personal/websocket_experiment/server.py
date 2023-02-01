import asyncio
import websockets

async def handler(websocket, path):
    while True:
        user_input = input("Enter a message to send to the client, or type 'exit' to quit: ")
        await websocket.send(user_input)

start_server = websockets.serve(handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()