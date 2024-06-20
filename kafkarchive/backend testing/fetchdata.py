import enka

retry = "y"

exportdict = {}

async def fetch() -> None:
    async with enka.HSRClient(headers=({"Kiryuuin":"school project website lmao"})) as client:
        userid = input("Please enter your UID : ")

        try:
            fetched = await client.fetch_showcase(userid)
        except enka.errors.PlayerDoesNotExistError:
            return print("player not found")
        except enka.errors.WrongUIDFormatError:
            return print("wrong uid format lol")
        except enka.errors.GameMaintenanceError:
            return print("game is in maintenance go touch grass lol")
        #print(f"Player name : {fetched.player.nickname}")
        #print(f"Player level : {fetched.player.level}")
        
        for char in fetched.characters:
            important_char_info = {}
            chardict = dict(id = char.id,
                            name = char.name,
                            level = char.level,
                            ascension = char.ascension
                            )
            important_char_info.update({"Character": chardict})

            lc = char.light_cone
            if lc is not None:
                lcdict = dict(id = lc.id,
                              name = lc.name,
                              level = lc.level,
                              ascension = lc.ascension)
                important_char_info.update({"Light cone": lcdict})
            else:
                important_char_info.update({"Light cone": None})

            chartrace = []
            for trace in char.traces:
                if trace.type-1 == 0:
                    chartrace.append(trace.id)
                important_char_info.update({"Traces list": chartrace})
            relictype = ["Head","Hands","Body","Feet","Planar Sphere","Link Rope"]
            dict_of_relics = {}
            for relic in char.relics:

                #print(relic.main_affix_id)
                relic_individ_dict = dict(setid = relic.set_id,
                                 setname = relic.set_name,
                                 level = relic.level,
                                 type = str(relic.rarity) + str(relic.type),
                                 rarity = str(relic.rarity),
                                 mainstat = str(relic.main_affix_id))
                """
                do something with sub_affix_list
                was going to continue programming but enka api is down and im sleepy
                """

                dict_of_relics.update({relictype[relic.type-1]: relic_individ_dict})
                
                important_char_info.update({"Relics":dict_of_relics})
                
                """
                make it somehow return substats info idk how
                """
                
            exportdict.update({char.id:important_char_info})
        return exportdict

"""
this file input is uid
output is character info, relic info, light cone info
"""