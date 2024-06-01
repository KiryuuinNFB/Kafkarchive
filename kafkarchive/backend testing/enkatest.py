import enka
import asyncio
import json

userid = input("Enter your UID: ")

async def main() -> None:
    async with enka.HSRClient("en", headers={"Kiryuuin":"testing"}) as client:
        fetched = await client.fetch_showcase(userid)

        print("Name ",fetched.player.nickname)
        print("Level ",fetched.player.level)

        for character in fetched.characters:
            fetchedlist = {}
            fetchedlist.update({"Character": character.name })
            for stat in character.stats:
                fetchedlist.update({stat.name: stat.formatted_value })
            lc = character.light_cone
            if lc is not None:
                for stats in lc.stats:
                    fetchedlist.update({"LC Name": lc.name})
                    fetchedlist.update({"LC" + stats.name: stats.formatted_value })


            for relic in character.relics:
                mainstat = relic.main_stat
                fetchedlist.update({relic.set_name + " " + str(relic.type) + " " + mainstat.name: mainstat.formatted_value})
            
            print(json.dumps(fetchedlist, indent=4, sort_keys=False))

asyncio.run(main())