import json
import asyncio
from fetchdata import *

async def main() -> None:
    response = await fetch()
    for chars in response:
        print(response[chars])
        with open(f"{chars}.json", 'w', encoding='utf-8') as f:
           json.dump(response[chars], f, ensure_ascii=False, indent=4)

asyncio.run(main())