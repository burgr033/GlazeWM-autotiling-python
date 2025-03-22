import asyncio
import websockets
import json


async def main():
    uri = "ws://localhost:6123"

    async with websockets.connect(uri) as websocket:

        await websocket.send("sub -e window_managed")

        while True:
            response = await websocket.recv()
            json_response = json.loads(response)
            try:
                sizePercentage = json_response["data"]["managedWindow"][
                    "tilingSize"
                ]
                if sizePercentage is None:
                    continue
                if sizePercentage <= 0.5:
                    await websocket.send('command toggle-tiling-direction')
            except KeyError:
                pass


if __name__ == "__main__":
    asyncio.run(main())
