import asyncio
import requests
import json

apiref = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
apirefshort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"

#what even
async def amogus_get_relicmain_database():
    response = requests.get(f"{apirefshort}relicMainStats.json")
    relicmaindatabase = response.json()
    return relicmaindatabase

async def amogus_stats_database():
    response = requests.get(f"{apiref}stats.json")
    statsdict = response.json()
    for stats in statsdict:
        
        print(json.dumps(statsdict[stats], indent=4, sort_keys=False))

async def amogus_chars_database():
    response = requests.get(f"{apiref}avatar.json")
    avtrdict = response.json()
    for chars in avtrdict:
        
        print(json.dumps(avtrdict[chars], indent=4, sort_keys=False))

async def amogus_relicmain_database():
    response = requests.get(f"{apirefshort}relicMainStats.json")
    relicmain = response.json()
    return relicmain
        
if __name__ == '__main__':
    asyncio.run(amogus_relicmain_database())

"""
please fix all of this. even if it means having another spaghetti code. but if it runs, it runs.
"""