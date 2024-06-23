from fetchdata import fetch
from amogus import *
import asyncio
import json

retry = "y"


async def main() -> None:
    enkafetched = await fetch()
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

            relicdict = eachchars["Relics"]
            dict_of_relics = {}
            for types in relicdict:

                relictype = relicdict[types]["type"]
                relicid = relicdict[types]["mainstat"]
                reliclevel = relicdict[types]["level"]
                calculatedrelic = await amogus_get_relic_main_from_type(relictype, relicid, reliclevel)
                
                dict_of_relics.update({types : calculatedrelic})

               
            """
            now format everything nicely
            """
                
        #print(json.dumps(enkafetched, indent=4, sort_keys=False))
            calculatedchar = await amogus_get_char_base_from_lvl(charid, charasc, charlvl)
            calculatedlc = await amogus_get_lc_base_from_lvl(lcid, lcsup, lclvl)
            calculated.update({"Char":charname})
            calculated.update({"Charstats":calculatedchar})
            calculated.update({"Light cone":lcname})
            calculated.update({"Light cone stats":calculatedlc})
            calculated.update({"Relics":dict_of_relics})
            
            print(json.dumps(calculated, indent=4, sort_keys=False))
        
    else:
        print("Enka API failed to fetch data")
    
    
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(main())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("Program Terminated")
            break

"""
the main file.

will order other files to get build infos and game data, look up values using wrapper and output the calculated stats
"""