import asyncio
import threading
import websockets

async def main():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            response = await websocket.recv()
            print(f"Received from server: {response}")

# asyncio.get_event_loop().run_until_complete(asyncio.create_task(main()))
# asyncio.get_event_loop().run_until_complete(main())
if __name__ == '__main__':
    thread = threading.Thread(target=asyncio.run, args=(main(),))
    thread.start()