from fetchdata import fetch
import asyncio
import json

retry = "y"

async def main() -> None:
    enkafetched = await fetch()
    #print(enkafetched)
    print(json.dumps(enkafetched, indent=4, sort_keys=False))
    #format the data better
    #nested dict



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