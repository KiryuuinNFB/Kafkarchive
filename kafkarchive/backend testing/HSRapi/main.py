from amogus import *
import asyncio

async def main():
    relicmain = await amogus_relicmain_database()
    #print(relicmain)
    print(relicmain["56"][1]["base"])
    print(relicmain["56"][1]["step"])
        
if __name__ == '__main__':
    asyncio.run(main())

"""
this is not the main backend file. this is the main file for the wrapper. import this file to the main backend file.
this file will get input such as character info, relic info, lc info and returns their values    
"""