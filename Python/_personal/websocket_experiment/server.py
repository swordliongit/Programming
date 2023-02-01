import asyncio
import websockets
 
connected_clients = {}
 
# create handler for each connection
 
async def handler(websocket, path):
    # Get the client identifier
    client_id = await websocket.recv()
    connected_clients[client_id] = websocket
    # await websocket.send(reply)
    if client_id == "client1":
        await connected_clients[client_id].send("Hello, client1!")
    elif client_id == "client2":
        await websocket.send("You are not client2!!")
 
start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()









# import asyncio
# import websockets
 
# # create handler for each connection

# async def handler(websocket, path):
#     # data = await websocket.recv()
#     # reply = f"Data recieved as:  {data}!"
#     reply = "Merhaba Client!"
#     await websocket.send(reply)
 
# start_server = websockets.serve(handler, "localhost", 8000)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()