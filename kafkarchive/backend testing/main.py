from fetchdata import fetch
from amogus import *
import asyncio
import json

retry = "y"

async def main() -> None:
    enkafetched = await fetch()
    if enkafetched is not None:

        #print(json.dumps(enkafetched, indent=4, sort_keys=False))
        charlvl = await amogus_get_char_base_from_lvl(1005, 6)
        print(json.dumps(charlvl, indent=4, sort_keys=False))
        for chars in enkafetched:
            print(chars)
    else:
        print("Enka API failed to fetch data")
    
    
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("bye lol")
            break

"""
the main file.

will order other files to get build infos and game data, look up values using wrapper and output the calculated stats
"""