import asyncio
import requests
import json

yattaapi = "https://api.yatta.top/hsr/v2/en/"
hsrmapapi = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
hsrmapapishort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"

#pulling data

async def amogus_stats_database():
   
    response = requests.get(f"{hsrmapapi}stats.json", timeout=60)
    
    statsdict = response.json()
    for stats in statsdict:
        
        print(json.dumps(statsdict[stats], indent=4, sort_keys=False))

async def amogus_chars_database(id):
    response = requests.get(f"{yattaapi}avatar/{id}")
    avtrdict = response.json()
    return avtrdict

async def amogus_lc_database(id):
    response = requests.get(f"{yattaapi}equipment/{id}")
    lcdict = response.json()
    return lcdict

async def amogus_relicmain_database():
    response = requests.get(f"{hsrmapapishort}relicMainStats.json")
    relmaindict = response.json()
    return relmaindict

async def amogus_relicsub_database():
    response = requests.get(f"{hsrmapapishort}relicSubStats.json")
    relsubdict = response.json()
    return relsubdict

async def amogus_relic_database():
    response = requests.get(f"{hsrmapapi}relicset.json")
    relsubdict = response.json()
    return relsubdict

async def amogus_hsrmap_chars_database(id):
    response = requests.get(f"{hsrmapapi}avatar.json")
    avtrdict = response.json()
    
    return avtrdict[str(id)]

#debug
async def testing():
    print("testing")
        
#pulling each values from the data

async def amogus_get_char_base_from_lvl(id, asc, lvl):
    charmain = await amogus_chars_database(id)

    basedict = charmain["data"]["upgrade"][asc]["skillBase"]
    adddict = charmain["data"]["upgrade"][asc]["skillAdd"]

    atkbase = basedict["attackBase"]
    atkadd = adddict["attackAdd"]

    defbase = basedict["defenceBase"]
    defadd = adddict["defenceAdd"]

    hpbase = basedict["hPBase"]
    hpadd = adddict["hPAdd"]

    spdbase = basedict["speedBase"]

    
    baseatkcalculated = atkbase + (atkadd*(lvl-1))
    basedefcalculated = defbase + (defadd*(lvl-1))
    basehpcalculated = hpbase + (hpadd*(lvl-1))
    basespdcalculated = spdbase
    

    calculatedcharbase = dict(CHAR_ATK = baseatkcalculated,
                              CHAR_DEF = basedefcalculated,
                              CHAR_HP = basehpcalculated,
                              CHAR_SPD = basespdcalculated)
    
    return calculatedcharbase

async def amogus_get_lc_base_from_lvl(id, asc, lvl, equip):
    if equip == True:
        lcmain = await amogus_lc_database(id)

        basedict = lcmain["data"]["upgrade"][asc]["skillBase"]
        adddict = lcmain["data"]["upgrade"][asc]["skillAdd"]

        atkbase = basedict["attackBase"]
        atkadd = adddict["attackAdd"]

        defbase = basedict["defenceBase"]
        defadd = adddict["defenceAdd"]

        hpbase = basedict["hPBase"]
        hpadd = adddict["hPAdd"]

        baseatkcalculated = atkbase + (atkadd*(lvl-1))
        basedefcalculated = defbase + (defadd*(lvl-1))
        basehpcalculated = hpbase + (hpadd*(lvl-1))
    

        calculatedlcbase = dict(LC_HP = basehpcalculated,
                                LC_ATK = baseatkcalculated,
                                LC_DEF = basedefcalculated)
    
        return calculatedlcbase
    else:
        emptylcbase = dict(LC_HP = 0,
                            LC_ATK = 0,
                            LC_DEF = 0)
        return emptylcbase
    

async def amogus_get_relic_main_from_type(type, id, lvl):
    relicmain = await amogus_relicmain_database()

    relicmaindict = relicmain[str(type)][id-1]

    reliccalculated = relicmaindict["base"] + (relicmaindict["step"]*lvl)
    relicsummary = dict(TYPE = relicmaindict["type"],
                        VALUE = reliccalculated)
    
    return relicsummary

async def amogus_get_relic_sub_from_subaffix(rarity, id, cnt, step):
    relicsub = await amogus_relicsub_database()

    relicsubdict = relicsub[rarity][id-1]

    relicsubcalculated = relicsubdict["base"]*cnt + relicsubdict["step"]*int(step or 0)
    relicsubsummary = dict(TYPE = relicsubdict["type"],
                           VALUE = relicsubcalculated)

    return relicsubsummary

async def amogus_get_trace_val_from_id(traceid):
    charid = str(traceid)[0:4]

    chardict = await amogus_hsrmap_chars_database(charid)
    for traces in chardict["tree"]:
        if traces["id"] == str(traceid):
            if str(traces["status"][0]["Value"])[0:1] == "0":
                flat = False
            else:
                flat = True
            indivi_trace = dict(TYPE = traces["status"][0]["PropertyType"],
                                VALUE = traces["status"][0]["Value"],
                                FLAT = flat)

    return indivi_trace

async def amogus_get_relic_bonus_from_id_and_count(relicid, count):
    relic = await amogus_relic_database()
    relicmain = relic[str(relicid)]

    active2 = dict(TYPE = None,
                   VALUE = 0)
    active4 = dict(TYPE = None,
                   VALUE = 0)
    activeempty = dict(TYPE = None,
                   VALUE = 0)

    for bonuses in relicmain["props"]: 
        if bonuses[0]["active"] == 2:
            active2["TYPE"] = bonuses[0]["type"]
            active2["VALUE"] = bonuses[0]["value"]
        elif bonuses[0]["active"] == 4:
            active4["TYPE"] = bonuses[0]["type"]
            active4["VALUE"] = bonuses[0]["value"]
    
    if count == 2 or count == 3:
        if active2["TYPE"] != None:
            result = dict(BONUS1 = active2, 
                          BONUS2 = activeempty)
        else:
            result = dict(BONUS1 = active4, 
                          BONUS2 = activeempty)
    elif count == 4:
        result = dict(BONUS1 = active2, 
                      BONUS2 = active4)
    elif count >= 1 or count < 4:
        result = dict(BONUS1 = activeempty, 
                      BONUS2 = activeempty)
        
    return result

if __name__ == '__main__':
    async def main() -> None:
        i = await amogus_chars_database(1005)
        print(json.dumps(i["data"]["name"], indent=4, sort_keys=False))

    asyncio.run(main())

"""
this file looks up game data
"""