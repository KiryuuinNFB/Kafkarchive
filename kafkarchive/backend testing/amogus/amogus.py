import asyncio
import requests
import json

yattaapi = "https://api.yatta.top/hsr/v2/en/"
hsrmapapi = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
hsrmapapishort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"



#pulling data

async def amogus_stats_database():
    response = requests.get(f"{hsrmapapi}stats.json")
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

async def amogus_get_lc_base_from_lvl(id, asc, lvl):
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

async def amogus_get_relic_main_from_type(type, id, lvl):
    relicmain = await amogus_relicmain_database()
    relicmaindict = relicmain[str(type)][id-1]

    reliccalculated = relicmaindict["base"]+(relicmaindict["step"]*lvl)
    return reliccalculated


"""
unfinished code
currently doing math about getting base stats from lvl with ascension factored in
"""
    

if __name__ == '__main__':
    async def main() -> None:
        i = await amogus_chars_database(1005)
        print(json.dumps(i["data"]["name"], indent=4, sort_keys=False))

    asyncio.run(main())

"""
this file looks up game data
"""