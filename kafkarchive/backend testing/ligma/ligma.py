import json
import asyncio

with open('sampleresults.json', 'r') as f:
    imported_dict = json.load(f)

flat_hp = []
hp_percent = []

flat_atk = []
atk_percent = []

flat_def = []
def_percent = []

flat_spd = []
spd_percent = []

async def list_sorting(dictwithval):
    match dictwithval["TYPE"]:
        case "HPDelta":
            flat_hp.append(dictwithval["VALUE"])
        case "HPAddedRatio":
            hp_percent.append(dictwithval["VALUE"])

        case "AttackDelta":
            flat_atk.append(dictwithval["VALUE"])
        case "AttackAddedRatio":
            atk_percent.append(dictwithval["VALUE"])

        case "DefenceDelta":
            flat_def.append(dictwithval["VALUE"])
        case "DefenceAddedRatio":
            def_percent.append(dictwithval["VALUE"])
        
        case "SpeedDelta":
            flat_spd.append(dictwithval["VALUE"])
        case "Speed":
            spd_percent.append(dictwithval["VALUE"])
        case _:
            pass

async def ligma_calculate_final(value_dict):
    global flat_hp
    global hp_percent
    global flat_atk
    global atk_percent
    global flat_def
    global def_percent
    global flat_spd
    global spd_percent

    flat_hp = []
    hp_percent = []
    flat_atk = []
    atk_percent = []
    flat_def = []
    def_percent = []
    flat_spd = [] 
    spd_percent = []

    base_hp = value_dict["Charstats"]["CHAR_HP"] + value_dict["Light cone stats"]["LC_HP"]
    base_atk = value_dict["Charstats"]["CHAR_ATK"] + value_dict["Light cone stats"]["LC_ATK"]
    base_def = value_dict["Charstats"]["CHAR_DEF"] + value_dict["Light cone stats"]["LC_DEF"]
    base_spd = value_dict["Charstats"]["CHAR_SPD"]

    relics = value_dict["Relics"]
    for types in relics:
        await list_sorting(relics[types])
        for substats in relics[types]["SUBSTATS"]:
            await list_sorting(relics[types]["SUBSTATS"][substats])

    traces = value_dict["Traces"]
    for eachtraces in traces:
        await list_sorting(traces[eachtraces])
             
    relic_bonus = value_dict["Relic bonuses"]
    for bonuses in relic_bonus:
        for bon1and2 in relic_bonus[bonuses]:
            await list_sorting(relic_bonus[bonuses][bon1and2])

    #print(flat_hp)
    #print(hp_percent)
    
    #hp formula
    #BASE HP*(1+SUM HP%)+SUM FLAT HP
    calculated_hp = round(base_hp, 3) * (1 + sum(hp_percent)) + sum(flat_hp)
    calculated_atk = round(base_atk, 3) * (1 + sum(atk_percent)) + sum(flat_atk)
    calculated_def = round(base_def, 3) * (1 + sum(def_percent)) + sum(flat_def)
    calculated_spd = base_spd * (1 + sum(spd_percent)) + sum(flat_spd)
    print(value_dict["Char"])
    print(round(calculated_hp, 3))
    print(round(calculated_atk, 3))
    print(round(calculated_def, 3))
    print(round(calculated_spd, 3))
    print("=====================")


async def main() -> None:
    for i in imported_dict:
        await ligma_calculate_final(imported_dict[i])

asyncio.run(main())

"""
only temporary
it is to test reading json files
"""