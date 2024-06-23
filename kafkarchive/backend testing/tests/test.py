import yatta
import asyncio
import json

async def main() -> None:
    async with yatta.YattaAPI() as client:
        fetched = await client.fetch_light_cone_detail(20000)
        print(fetched)

asyncio.run(main())