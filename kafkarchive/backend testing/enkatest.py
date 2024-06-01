import enka
import asyncio
import json

userid = input("Enter your UID: ")

async def main() -> None:
    async with enka.HSRClient("en", headers={"Kiryuuin":"testing for a school project website"}) as client:
        fetched = await client.fetch_showcase(userid)
        print("Name ",fetched.player.nickname)
        print("Level ",fetched.player.level)
        for character in fetched.characters:
            fetchedlist = {}
            hp_percent = []
            flat_hp = []
            fetchedlist.update({"Character": character.name })
            for stat in character.stats:
                fetchedlist.update({stat.name: stat.formatted_value })
            lc = character.light_cone
            if lc is not None:
                for stats in lc.stats:
                    fetchedlist.update({"LC Name": lc.name})
                    fetchedlist.update({"LC" + stats.name: stats.formatted_value })
            relictype = ["Head","Hands","Body","Feet","Planar Sphere","Link Rope"]
            for relic in character.relics:
                mainstat = relic.main_stat
                fetchedlist.update({relictype[relic.type-1]:relic.set_name})
                fetchedlist.update({relictype[relic.type-1] + " " + mainstat.name: mainstat.formatted_value})
                if mainstat.name == "HP" and mainstat.formatted_value.endswith("%"):
                    hp_percent.append(float(mainstat.formatted_value.replace("%","")))
                if mainstat.name == "HP" and not mainstat.formatted_value.endswith("%"):
                    flat_hp.append(int(mainstat.formatted_value))
                

                substatnum = 0
                for substats in relic.sub_stats:
                    substatnum = substatnum + 1
                    fetchedlist.update({substats.name + " " + relictype[relic.type-1] + " "+ str(substatnum): substats.formatted_value})
                    if substats.name == "HP" and substats.formatted_value.endswith("%"):
                        hp_percent.append(float(substats.formatted_value.replace("%","")))
                    if substats.name == "HP" and not substats.formatted_value.endswith("%"):
                        flat_hp.append(int(substats.formatted_value))
            
            summed_hp_percent = sum(hp_percent)
            summed_flat_hp = int(sum(flat_hp))
            print(json.dumps(fetchedlist, indent=4, sort_keys=False))

            #please fix
            #calculated_hp = (int(fetchedlist["Base HP"]) + int(fetchedlist["LCBase HP"]))*(1+(summed_hp_percent*0.01)) + summed_flat_hp
            #print(calculated_hp)
asyncio.run(main())
