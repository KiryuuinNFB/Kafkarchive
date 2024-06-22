from fetchdata import fetch
from amogus import *
import asyncio
import json

retry = "y"


async def main() -> None:
    enkafetched = await fetch()
    if enkafetched is not None:
        for chars in enkafetched:
            eachchars = enkafetched[chars]
            
            
            charid = eachchars["Character"]["id"]
            charasc = eachchars["Character"]["ascension"]
            charlvl = eachchars["Character"]["level"]
                
        #print(json.dumps(enkafetched, indent=4, sort_keys=False))
            charbase = await amogus_get_char_base_from_lvl(charid, charasc, charlvl)
            print(json.dumps(charbase, indent=4, sort_keys=False))
        
    else:
        print("Enka API failed to fetch data")
    
    
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("bye lol")
            break

"""
the main file.

will order other files to get build infos and game data, look up values using wrapper and output the calculated stats
"""