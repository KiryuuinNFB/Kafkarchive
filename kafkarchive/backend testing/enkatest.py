import enka
import asyncio
import json
import yatta

userid = input("Enter your UID: ")

charaid = 1005

async def main() -> None:
    async with enka.HSRClient("en", headers={"Kiryuuin":"testing for a school project website"}) as client:
        fetched = await client.fetch_showcase(userid)
        print("Name ",fetched.player.nickname)
        print("Level ",fetched.player.level)

        for character in fetched.characters:

            fetchedlist = {}

            hp_percent = []
            flat_hp = []

            atk_percent = []
            flat_atk = []

            def_percent = []
            flat_def = []

            spd_percent = []
            flat_spd = []

            hptrace = {}
            atktrace = {}
            deftrace = {}
            spdtrace = {}

            traceval = {}
            """
            yattaapi = yatta.YattaAPI(headers={"Kiryuuin":"testing for a school project website"})
            await yattaapi.start()
            fromyatta = await yattaapi.fetch_character_detail(character.id)
            traceval = {}
            for yattatrace in fromyatta.traces.sub_skills:
                #print(yattatrace.name)
                #print(yattatrace.id)
                for stats in yattatrace.status_list:
                    traceval.update({yattatrace.id:stats.value})
                    if "HP" in yattatrace.name:
                        hptrace.update({yattatrace.id:float(traceval[yattatrace.id])})
                    elif "ATK" in yattatrace.name:
                        atktrace.update({yattatrace.id:float(traceval[yattatrace.id])})
                    elif "DEF" in yattatrace.name:
                        deftrace.update({yattatrace.id:float(traceval[yattatrace.id])})
                    elif "SPD" in yattatrace.name:
                        spdtrace.update({yattatrace.id:float(traceval[yattatrace.id])})
            
            await yattaapi.close()
            """
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
                elif mainstat.name == "DEF" and mainstat.is_percentage==True:
                    def_percent.append(float(mainstat.formatted_value.replace("%","")))
                elif mainstat.name == "SPD" and mainstat.is_percentage==True:
                    spd_percent.append(float(mainstat.formatted_value.replace("%","")))
                if mainstat.name == "HP" and mainstat.is_percentage==False:
                    flat_hp.append(int(mainstat.formatted_value))
                elif mainstat.name == "ATK" and mainstat.is_percentage==False:
                    flat_atk.append(int(mainstat.formatted_value))
                elif mainstat.name == "DEF" and mainstat.is_percentage==False:
                    flat_def.append(int(mainstat.formatted_value))
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
                    elif substats.name == "DEF" and substats.is_percentage==True:
                        def_percent.append(float(substats.formatted_value.replace("%","")))
                    elif substats.name == "SPD" and substats.is_percentage==True:
                        spd_percent.append(float(substats.formatted_value.replace("%","")))
                    if substats.name == "HP" and substats.is_percentage==False:
                        flat_hp.append(int(substats.formatted_value))
                    elif substats.name == "ATK" and substats.is_percentage==False:
                        flat_atk.append(int(substats.formatted_value))
                    elif substats.name == "DEF" and substats.is_percentage==False:
                        flat_def.append(int(substats.formatted_value))
                    elif substats.name == "SPD" and substats.is_percentage==False:
                        flat_spd.append(float(substats.formatted_value))
            
                #working on it, im having a brain aneurysm
            """
            tracetype = ["STAT","SKILL","TALENT"]
            charatraces = {}

            chara_hp_trace = []
            chara_atk_trace = []
            chara_def_trace = []
            chara_spd_trace = []

            for traceid in character.traces:
                if traceid.type-1 == 0:
                    charatraces.update({tracetype[traceid.type-1]: traceid.id})

                    if charatraces[traceid.id] in hptrace:
                        try:
                            chara_hp_trace.append(float(hptrace))
                        except KeyError:
                            raise
                    elif charatraces[traceid.id] in atktrace:
                        try:
                            chara_atk_trace.append(float(atktrace))
                        except KeyError:
                            raise
                    elif charatraces[traceid.id] in deftrace:
                        try:
                            chara_def_trace.append(float(deftrace))
                        except KeyError:
                            raise
                    elif charatraces[traceid.id] in spdtrace:
                        try:
                            chara_spd_trace.append(float(spdtrace))
                        except KeyError:
                            raise
                    #print(json.dumps(charatraces, indent=4, sort_keys=False))
            print(chara_hp_trace)
            print(chara_atk_trace)
            print(chara_def_trace)
            print(chara_spd_trace)
            
            """
            
            summed_hp_percent = sum(hp_percent)
            summed_flat_hp = int(sum(flat_hp))

            summed_atk_percent = sum(atk_percent)
            summed_flat_atk = int(sum(flat_atk))

            summed_def_percent = sum(def_percent)
            summed_flat_def = int(sum(flat_def))

            summed_spd_percent = sum(spd_percent)
            summed_flat_spd = float(sum(flat_spd))

            
            
            #please fetch traces data. already did
            print("==========================")
            print(character.name)
            #print(spd_percent)

            #BASE HP*(1+SUM HP%)+SUM FLAT HP 
            calculated_hp = (int(fetchedlist["Base HP"])) * (1+(summed_hp_percent/100)) + summed_flat_hp
            print(f"HP: {int(fetchedlist["HP"])}")
            print(f"Calculated HP: {calculated_hp}")
            print(f"ΔHP:{(int(fetchedlist["HP"])) - calculated_hp}")
            #BASE ATK*(1+SUM ATK%)+SUM FLAT ATK
            calculated_atk = (int(fetchedlist["Base ATK"])) * (1+(summed_atk_percent/100)) + summed_flat_atk
            print(f"ATK: {int(fetchedlist["ATK"])}")
            print(f"Calculated ATK: {calculated_atk}")
            print(f"ΔATK:{(int(fetchedlist["ATK"])) - calculated_atk}")
            #BASE DEF*(1+SUM DEF%)+SUM FLAT DEF
            calculated_def = (int(fetchedlist["Base DEF"])) * (1+(summed_def_percent/100)) + summed_flat_def
            print(f"DEF: {int(fetchedlist["DEF"])}")
            print(f"Calculated DEF: {calculated_def}")
            print(f"ΔDEF:{(int(fetchedlist["DEF"])) - calculated_def}")
            #BASE SPD*(1+SUM SPD%)+SUM FLAT SPD
            calculated_spd = (float(fetchedlist["SPD"])) * (1+summed_spd_percent/100) + summed_flat_spd
            print(f"Calculated SPD: {calculated_spd}")
            print(json.dumps(fetchedlist, indent=4, sort_keys=False))
            

asyncio.run(main())