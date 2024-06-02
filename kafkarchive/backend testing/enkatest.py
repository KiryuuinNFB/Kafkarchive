import enka
import asyncio
import json

userid = input("Enter your UID: ")


async def main() -> None:
    async with enka.HSRClient("en", headers={"Kiryuuin":"testing for a school project website"}) as client:
        fetched = await client.fetch_showcase(userid)
        #print(type(fetched))
        print("Name ",fetched.player.nickname)
        print("Level ",fetched.player.level)
        for character in fetched.characters:
            fetchedlist = {}

            hp_percent = []
            flat_hp = []

            atk_percent = []
            flat_atk = []

            spd_percent = []
            flat_spd = []

            fetchedlist.update({"Character": character.name })
            for stat in character.stats:
                fetchedlist.update({stat.name: stat.formatted_value })
            lc = character.light_cone
            if lc is not None:
                for stats in lc.stats:
                    fetchedlist.update({"LC Name": lc.name})
                    fetchedlist.update({"LC" + stats.name: stats.formatted_value })
            else: #why would you not use a lc lmao
                fetchedlist.update({"LCBase HP": 0 })
                fetchedlist.update({"LCBase ATK": 0 })
                fetchedlist.update({"LCBase DEF": 0 })

            relictype = ["Head","Hands","Body","Feet","Planar Sphere","Link Rope"]
            for relic in character.relics:
                mainstat = relic.main_stat
                fetchedlist.update({relictype[relic.type-1]:relic.set_name})
                fetchedlist.update({relictype[relic.type-1] + " " + mainstat.name: mainstat.formatted_value})
                if mainstat.name == "HP" and mainstat.is_percentage==True:
                    hp_percent.append(float(mainstat.formatted_value.replace("%","")))
                elif mainstat.name == "ATK" and mainstat.is_percentage==True:
                    atk_percent.append(float(mainstat.formatted_value.replace("%","")))
                elif mainstat.name == "SPD" and mainstat.is_percentage==True:
                    spd_percent.append(float(mainstat.formatted_value.replace("%","")))
                if mainstat.name == "HP" and mainstat.is_percentage==False:
                    flat_hp.append(int(mainstat.formatted_value))
                elif mainstat.name == "ATK" and mainstat.is_percentage==False:
                    flat_atk.append(int(mainstat.formatted_value))
                elif mainstat.name == "SPD" and mainstat.is_percentage==False:
                    flat_spd.append(float(mainstat.formatted_value))
                
                
                substatnum = 0
                for substats in relic.sub_stats:
                    substatnum = substatnum + 1
                    fetchedlist.update({substats.name + " " + relictype[relic.type-1] + " "+ str(substatnum): substats.formatted_value})
                    if substats.name == "HP" and substats.is_percentage==True:
                        hp_percent.append(float(substats.formatted_value.replace("%","")))
                    elif substats.name == "ATK" and substats.is_percentage==True:
                        atk_percent.append(float(substats.formatted_value.replace("%","")))
                    elif substats.name == "SPD" and substats.is_percentage==True:
                        spd_percent.append(float(substats.formatted_value.replace("%","")))
                    if substats.name == "HP" and substats.is_percentage==False:
                        flat_hp.append(int(substats.formatted_value))
                    elif substats.name == "ATK" and substats.is_percentage==False:
                        flat_atk.append(int(substats.formatted_value))
                    elif substats.name == "SPD" and substats.is_percentage==False:
                        flat_spd.append(float(substats.formatted_value))
                #working on it, im having a brain aneurysm
            #print(type(character.traces))
            
            #print("\n".join([str(i) for i in character.traces]))

            summed_hp_percent = sum(hp_percent)
            summed_flat_hp = int(sum(flat_hp))

            summed_atk_percent = sum(atk_percent)
            summed_flat_atk = int(sum(flat_atk))

            summed_spd_percent = sum(spd_percent)
            summed_flat_spd = float(sum(flat_spd))

            #please fetch traces data
            print(character.name)
            print(flat_hp)

            #(BASE HP)*

            calculated_hp = (int(fetchedlist["Base HP"]))*(1+(summed_hp_percent/100)) + summed_flat_hp
            print(f"HP: {calculated_hp}")
            calculated_atk = (int(fetchedlist["Base ATK"]))*(1+(summed_atk_percent/100)) + summed_flat_atk
            print(f"ATK: {calculated_atk}")
            calculated_spd = (float(fetchedlist["SPD"])) * (1+summed_spd_percent)+summed_flat_spd
            print(f"SPD: {calculated_spd}")
            
            #print(json.dumps(fetchedlist, indent=4, sort_keys=False))
asyncio.run(main())