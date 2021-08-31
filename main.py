#!/usr/bin/env python

import asyncio
import websockets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

start_server = websockets.serve(echo, "localhost", args.port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()