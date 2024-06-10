import enka
import asyncio
import json

retry = "y"

async def main() -> None:
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
        important_char_info = {}
        for char in fetched.characters:
            important_char_info.update({"Char name":char.name})
            important_char_info.update({"Char lvl":char.level})
            important_char_info.update({"Char id":char.id})

            lc = char.light_cone
            if lc is not None:
                important_char_info.update({"Light cone id":lc.id})
                important_char_info.update({"Light cone lvl":lc.level})
            else:
                important_char_info.update({"Light cone name":"Not equipped"})
                important_char_info.update({"Light cone lvl":0})
            relictype = ["Head","Hands","Body","Feet","Planar Sphere","Link Rope"]
            for relic in char.relics:
                important_char_info.update({relictype[relic.type-1]:relic.set_id})

            print(json.dumps(important_char_info, indent=4, sort_keys=False))
        
#if __name__ == '__main__':
while retry.lower() == "y":
    asyncio.run(main())
    retry = input("again? [Y/N] :")
    if retry.lower() == "n":
        print("bye lol")
        break