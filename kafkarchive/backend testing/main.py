from fetchdata import fetch
import asyncio
import json

retry = "y"

async def main() -> None:
    enkafetched = await fetch()
    print(json.dumps(enkafetched, indent=4, sort_keys=False))

if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("bye lol")
            break