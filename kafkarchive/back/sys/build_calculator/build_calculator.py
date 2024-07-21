
from .amogus import *
from .ligma import *

import asyncio
import json
import timeit

retry = "y"

async def build_calculation(builddata) -> None:
    start = timeit.default_timer()
    #allasjson = {}
    #print(json.dumps(builddata, indent=4, sort_keys=False))
    if builddata is not None:
        calculated = {}
        eachchars = builddata
        charname = eachchars["Character"]["name"]

        charid = eachchars["Character"]["id"]
        charasc = eachchars["Character"]["ascension"]
        charlvl = eachchars["Character"]["level"]

        lcname = eachchars["Light_cone"]["name"]

        lcid = eachchars["Light_cone"]["id"]
        lcsup = eachchars["Light_cone"]["ascension"]
        lclvl = eachchars["Light_cone"]["level"]
        lcequip = eachchars["Light_cone"]["equipped"]

        traces = eachchars["Traces_list"]

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

            list_of_substats = []

            for substats in relicdict[types]["substats"]:
                temp_index = relicdict[types]["substats"].index(substats)
                #haha nested dictionary go brrrrrr
                #haha restructuring data type go brrrrrr
                substat_id = relicdict[types]["substats"][temp_index]["id"]
                substat_cnt = relicdict[types]["substats"][temp_index]["cnt"]
                substat_step = relicdict[types]["substats"][temp_index]["step"]

                calculatedsubstats = await amogus_get_relic_sub_from_subaffix(relicrarity, substat_id, substat_cnt, substat_step)
                list_of_substats.append(calculatedsubstats)
            calculatedrelic.update({"SUBSTATS":list_of_substats})
            list_of_relic_bonus.append(relicsetid)
        dict_of_relic_bonus = {i:list_of_relic_bonus.count(i) for i in list_of_relic_bonus}
        for sets in dict_of_relic_bonus:
            fetchedrelbonus = await amogus_get_relic_bonus_from_id_and_count(sets, dict_of_relic_bonus[sets])
            dict_of_calculated_bonus.update({sets:fetchedrelbonus})
        
        calculatedchar = await amogus_get_char_base_from_lvl(charid, charasc, charlvl)
            
        calculatedlc = await amogus_get_lc_base_from_lvl(lcid, lcsup, lclvl, lcequip)
        calculated.update({"Char":charname})
        calculated.update({"Charstats":calculatedchar})
        calculated.update({"Light_cone":lcname})
        calculated.update({"Light_cone_stats":calculatedlc})
        calculated.update({"Relics": dict_of_relics})
        calculated.update({"Traces": dict_of_traces})
        calculated.update({"Relic_bonuses": dict_of_calculated_bonus})

            #with open("zkungsampleresult.json",'w', encoding='utf-8') as f:
            #    json.dump(calculated, f, indent=4, ensure_ascii=False)
        final = await ligma_calculate_final(calculated)
        stop = timeit.default_timer()
        print('Time elapsed ', round(stop - start,3), "seconds")
        
        #print(json.dumps(calculated, indent=4, sort_keys=False))
        return final
            #allasjson.update({chars:calculated})

    else:
        print("Enka API failed to fetch data")

async def forward_amogus_get_chars_data(datatype):
    return await amogus_get_chars_data(datatype)

async def forward_amogus_get_relic_data(datatype):
    return await amogus_get_relic_data(datatype)

async def forward_amogus_get_lc_data(datatype):
    return await amogus_get_lc_data(datatype)
    
    
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(build_calculation())
        retry = input("again? [Y/N] :")
        if retry.lower() != "y":
            print("Program Terminated")
            break

"""
the main file.

will order other files to get build infos and game data, look up values using wrapper and output the calculated stats
"""