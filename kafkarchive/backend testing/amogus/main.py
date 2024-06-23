from amogus import *
import json
import asyncio

async def main() -> None:
    result = await amogus_get_relic_main_from_type(51, 1, 15)
    print(json.dumps(result, indent=4, sort_keys=False))

asyncio.run(main())