import asyncio
import requests
import json

apiref = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
apirefshort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"

#pulling data

async def amogus_stats_database():
    response = requests.get(f"{apiref}stats.json")
    statsdict = response.json()
    for stats in statsdict:
        
        print(json.dumps(statsdict[stats], indent=4, sort_keys=False))

async def amogus_chars_database():
    response = requests.get(f"{apiref}avatar.json")
    avtrdict = response.json()
    return avtrdict

async def amogus_relicmain_database():
    response = requests.get(f"{apirefshort}relicMainStats.json")
    relicmain = response.json()
    return relicmain

#debug

async def testing():
    print("testing")
        
#pulling each values from the data

async def amogus_get_char_base_from_lvl(id, asc, lvl):
    charmain = await amogus_chars_database()
    basestatsdict = charmain[str(id)]["statsArray"][asc]
    
    return basestatsdict
"""
unfinished code
currently doing math about getting base stats from lvl with ascension factored in
"""
    

if __name__ == '__main__':
    asyncio.run(amogus_relicmain_database())

"""
this file looks up game data
"""