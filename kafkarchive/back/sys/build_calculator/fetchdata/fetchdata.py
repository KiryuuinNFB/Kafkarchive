import enka

retry = "y"

async def fetch(userid) -> None:
    async with enka.HSRClient(headers=({"Kiryuuin":"school project website lmao"})) as client:
        

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
        exportdict = {}
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
                              ascension = lc.ascension,
                              equipped = True)
                important_char_info.update({"Light_cone": lcdict})
            else:
                lcemptydict = dict(id = 0,
                                   name = "NOT EQUIPPED",
                                   level = 0,
                                   ascension = 0,
                                   equipped = False)
                important_char_info.update({"Light_cone": lcemptydict})

            chartrace = []
            for trace in char.traces:
                if trace.type-1 == 0:
                    chartrace.append(trace.id)
                important_char_info.update({"Traces_list": chartrace})
            relictype = ["Head","Hands","Body","Feet","Planar_Sphere","Link_Rope"]
            dict_of_relics = {}
            for relic in char.relics:
                
                relic_sub = relic.sub_affix_list
                list_of_substats = []

                for substats in relic_sub:
                    
                    relic_substats_dict = dict(id = substats.id,
                                               cnt = substats.cnt,
                                               step = substats.step)
                    list_of_substats.append(relic_substats_dict)

                relic_individ_dict = dict(setid = relic.set_id,
                                          setname = relic.set_name,
                                          level = relic.level,
                                          type = str(relic.rarity) + str(relic.type),
                                          rarity = str(relic.rarity),
                                          mainstat = relic.main_affix_id,
                                          actualtype = str(relic.type),
                                          substats = list_of_substats)
                """
                what tf did i do but now it works for some reason
                """

                dict_of_relics.update({relictype[relic.type-1]: relic_individ_dict})
                
                important_char_info.update({"Relics":dict_of_relics})

                #return important_char_info
            exportdict.update({str(char.id):important_char_info})
        return exportdict
        

"""
this file input is uid
output is character info, relic info, light cone info
"""