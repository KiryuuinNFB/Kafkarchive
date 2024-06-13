import enka
import asyncio
import json

retry = "y"

async def fetch() -> None:
    async with enka.HSRClient(headers=({"Kiryuuin":"rewriting the spaghetti code"})) as client:
        userid = input("Please enter your UID : ")

        try:
            fetched = await client.fetch_showcase(userid)
        except enka.errors.PlayerDoesNotExistError:
            return print("player not found")
        except enka.errors.WrongUIDFormatError:
            return print("wrong uid format lol")
        except enka.errors.GameMaintenanceError:
            return print("game is in maintenance go touch grass lol")
        print(f"Player name : {fetched.player.nickname}")
        print(f"Player level : {fetched.player.level}")
        
        for char in fetched.characters:
            important_char_info = {}

            important_char_info.update({"Char name":char.name})
            important_char_info.update({"Char lvl":char.level})
            important_char_info.update({"Char asc":char.ascension})
            important_char_info.update({"Char id":char.id})

            lc = char.light_cone
            if lc is not None:
                important_char_info.update({"Light cone id":lc.id})
                important_char_info.update({"Light cone lvl":lc.level})
                important_char_info.update({"Light cone asc":lc.ascension})
            else:
                important_char_info.update({"Light cone name":"Not equipped"})
                important_char_info.update({"Light cone lvl":0})

            important_char_info.update({"===================traces=====":"=====traces=============="})
            chartrace = []
            for trace in char.traces:
                if trace.type-1 == 0:
                    chartrace.append(trace.id)
                important_char_info.update({"Traces list": chartrace})

            important_char_info.update({"===================relic=====":"=====relic=============="})
            relictype = ["Head","Hands","Body","Feet","Planar Sphere","Link Rope"]
            print(char.name)
            for relic in char.relics:
                
                print(relictype[relic.type-1]) 
                print(relic.set_name)
                print(relic.main_affix_id)
                print(relic.sub_affix_list)
                
                #important_char_info.update({relic.id:" "})
                #important_char_info.update({relic.set_id:" "})
            
                    
            return important_char_info
            #print(json.dumps(important_char_info, indent=4, sort_keys=False))
        
if __name__ == '__main__':
    while retry.lower() == "y":
        asyncio.run(fetch())
        retry = input("again? [Y/N] :")
        if retry.lower() == "n":
            print("bye lol")
            break