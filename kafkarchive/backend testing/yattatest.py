import yatta
import asyncio
import json

async def main() -> None:
    async with yatta.YattaAPI(headers={"Kiryuuin":"testing for a school project website"}) as client:
        fetched = await client.fetch_light_cones()
        #print(fetched)
        for lc in fetched:
            fetchedlist = {}
            fetchedlist.update({"Name": lc.name})
            for data in lc.name:
                fetchedlist.update({data: str(lc.id)})
            
        print(json.dumps(fetchedlist, indent=4, sort_keys=False))

asyncio.run(main())