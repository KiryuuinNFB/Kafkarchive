from fetchdata import fetch
import yatta
import asyncio
import json

retry = "y"

async def main() -> None:
    #await fetch()
    async with yatta.YattaAPI(headers=({"Kiryuuin":"rewriting the spaghetti code"})) as clienty:
        yattafetched = await clienty.fetch_relic_set_detail(116)
        #print(json.dumps(yattafetched, indent=4, sort_keys=False))
        print(yattafetched)

if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("bye lol")
            break
