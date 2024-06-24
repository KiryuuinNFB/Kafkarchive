from amogus import *
import json
import asyncio

async def main() -> None:
    result = await amogus_hsrmap_chars_database(1005)
    print(json.dumps(result, indent=4, sort_keys=False))

asyncio.run(main())