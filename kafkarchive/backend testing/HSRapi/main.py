from amogus import amogus_relicmain_database
import asyncio

async def main():
    relicmain = await amogus_relicmain_database()
    #print(relicmain)
    print(relicmain["56"][1]["base"])
    print(relicmain["56"][1]["step"])
        
    

if __name__ == '__main__':
    asyncio.run(main())