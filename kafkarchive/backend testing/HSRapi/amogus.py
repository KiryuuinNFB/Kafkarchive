import asyncio
import requests
import json

apiref = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
apirefshort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"

async def amogus_fetch_stats():
    response = requests.get(f"{apiref}stats.json")
    statsdict = response.json()
    for stats in statsdict:
        
        print(json.dumps(statsdict[stats], indent=4, sort_keys=False))

async def amogus_fetch_chars():
    response = requests.get(f"{apiref}avatar.json")
    avtrdict = response.json()
    for chars in avtrdict:
        
        print(json.dumps(avtrdict[chars], indent=4, sort_keys=False))

async def amogus_fetch_relicmain():
    response = requests.get(f"{apirefshort}relicMainStats.json")
    relicmaindict = response.json()
    print(json.dumps(relicmaindict, indent=4, sort_keys=False))
        
asyncio.run(amogus_fetch_relicmain())

"""
please fix all of this. even if it means having another spaghetti code. but if it runs, it runs.
"""