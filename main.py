#!/usr/bin/env python

import asyncio
import websockets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()

print("Starting websocket server")

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

start_server = websockets.serve(echo, "0.0.0.0", args.port)
print("Started websocket server on port: " + args.port);

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()