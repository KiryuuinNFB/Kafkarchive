from fetchdata import fetch
import asyncio
import json

retry = "y"

async def main() -> None:
    enkafetched = await fetch()
    if enkafetched is not None:

        print(json.dumps(enkafetched, indent=4, sort_keys=False))
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