import json
import asyncio
from build_calculator.fetchdata import *
from build_calculator import *

async def main() -> None:
    userid = input("Please enter your UID : ")
    data = await fetch(userid)
    for chars in data:
        response = await build_calculation(data[str(chars)], "raw")
        with open(f"{chars}.json", 'w', encoding='utf-8') as f:
           json.dump(response, f, ensure_ascii=False, indent=4)

asyncio.run(main())