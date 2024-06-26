from fetchdata import fetch
from amogus import *
import asyncio
import json
import timeit

retry = "y"

async def main() -> None:
    enkafetched = await fetch()
    start = timeit.default_timer()
    #print(json.dumps(enkafetched, indent=4, sort_keys=False))
    if enkafetched is not None:
        for chars in enkafetched:
            calculated = {}
            eachchars = enkafetched[chars]
            charname = eachchars["Character"]["name"]
            
            charid = eachchars["Character"]["id"]
            charasc = eachchars["Character"]["ascension"]
            charlvl = eachchars["Character"]["level"]

            lcname = eachchars["Light cone"]["name"]

            lcid = eachchars["Light cone"]["id"]
            lcsup = eachchars["Light cone"]["ascension"]
            lclvl = eachchars["Light cone"]["level"]
            lcequip = eachchars["Light cone"]["equipped"]

            traces = eachchars["Traces list"]

            dict_of_traces = {}
            for traceid in traces:
                
                trace_data = await amogus_get_trace_val_from_id(traceid)
                dict_of_traces.update({traceid:trace_data})

            relicdict = eachchars["Relics"]
            dict_of_relics = {}
            list_of_relic_bonus = []
            dict_of_calculated_bonus = {}
            for types in relicdict:

                relictype = relicdict[types]["type"]
                relicid = relicdict[types]["mainstat"]
                reliclevel = relicdict[types]["level"]
                relicrarity = relicdict[types]["rarity"]

                relicsetid = relicdict[types]["setid"]

                calculatedrelic = await amogus_get_relic_main_from_type(relictype, relicid, reliclevel)
                
                dict_of_relics.update({types : calculatedrelic})

                dict_of_substats = {}

                for substats in relicdict[types]["substats"]:
                    #haha nested dictionary go brrrrrr
                    substat_id = relicdict[types]["substats"][substats]["id"]
                    substat_cnt = relicdict[types]["substats"][substats]["cnt"]
                    substat_step = relicdict[types]["substats"][substats]["step"]

                    calculatedsubstats = await amogus_get_relic_sub_from_subaffix(relicrarity, substat_id, substat_cnt, substat_step)
                    dict_of_substats.update({substats:calculatedsubstats})
                calculatedrelic.update({"SUBSTATS":dict_of_substats})
                list_of_relic_bonus.append(relicsetid)
            dict_of_relic_bonus = {i:list_of_relic_bonus.count(i) for i in list_of_relic_bonus}
            for sets in dict_of_relic_bonus:
                fetchedrelbonus = await amogus_get_relic_bonus_from_id_and_count(sets, dict_of_relic_bonus[sets])
                dict_of_calculated_bonus.update({sets:fetchedrelbonus})
        
            calculatedchar = await amogus_get_char_base_from_lvl(charid, charasc, charlvl)
            
            calculatedlc = await amogus_get_lc_base_from_lvl(lcid, lcsup, lclvl, lcequip)
            calculated.update({"Char":charname})
            calculated.update({"Charstats":calculatedchar})
            calculated.update({"Light cone":lcname})
            calculated.update({"Light cone stats":calculatedlc})
            calculated.update({"Relics": dict_of_relics})
            calculated.update({"Traces": dict_of_traces})
            calculated.update({"Relic bonuses": dict_of_calculated_bonus})
            
            print(json.dumps(calculated, indent=4, sort_keys=False))
        
        stop = timeit.default_timer()
        print('Time elapsed ', round(stop - start,3), "seconds")  

    else:
        print("Enka API failed to fetch data")
    
    
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() != "y":
            print("Program Terminated")
            break

"""
the main file.

will order other files to get build infos and game data, look up values using wrapper and output the calculated stats
"""