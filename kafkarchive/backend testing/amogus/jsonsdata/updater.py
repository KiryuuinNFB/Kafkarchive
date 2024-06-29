import json
import requests
import asyncio

yattaapi = "https://api.yatta.top/hsr/v2/en/"
hsrmapapi = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
hsrmapapishort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"

"""
simple updaters
"""

async def update_stats():
    print("updating stats.json")
    response = requests.get(f"{hsrmapapi}stats.json")
    with open("stats.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated stats.json")
 
async def update_relic_main():
    print("updating relicMainStats.json")
    response = requests.get(f"{hsrmapapishort}relicMainStats.json")
    with open("relicMainStats.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated relicMainStats.json")

async def update_relic_sub():
    print("updating relicSubStats.json")
    response = requests.get(f"{hsrmapapishort}relicSubStats.json")
    with open("relicSubStats.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated relicSubStats.json")

async def update_relics():
    print("updating relicsets.json")
    response = requests.get(f"{hsrmapapi}relicset.json")
    with open("relicsets.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated relicsets.json")
"""
chars updater
"""

async def get_all_avtr_id():
    response = requests.get(f"{hsrmapapi}avatar.json")
    id_lists = list(())
    for ids in response.json():
        
        if ids != "maxLevels":
            id_lists.append(ids)
        else:
            pass
    return id_lists

async def get_avatar_info(id):
    response = requests.get(f"{yattaapi}avatar/{id}")
    return response.json()

async def update_avatar():
    print("updating avatar.json")
    avtr_dict = dict()
    id_lists = await get_all_avtr_id()
    for ids in id_lists:
        avtrinfo = await get_avatar_info(ids)
        avtr_dict.update({ids : avtrinfo})
        if avtrinfo.get("response") == None:
            print(f"character with id {ids} not found")
        else:
            print(f"updating {avtrinfo["data"]["name"]}")
    with open("avatar.json", 'w', encoding='utf-8') as f:
        json.dump(avtr_dict, f, ensure_ascii=False, indent=4)
        print("Successfully updated avatar.json")

"""
chars hsrmap updater
"""

async def update_chars():
    response = requests.get(f"{hsrmapapi}avatar.json")
    with open("chars.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated chars.json")

"""
light cone updater
"""

async def get_all_lc_id():
    response = requests.get(f"{hsrmapapi}weapons.json")
    id_lists = list(())
    for ids in response.json():
            id_lists.append(ids)
    return id_lists

async def get_lc_info(id):
    response = requests.get(f"{yattaapi}equipment/{id}")
    return response.json()

async def update_light_cone():
    print("updating lightCone.json")
    lc_dict = dict()
    id_lists = await get_all_lc_id()
    for ids in id_lists:
        lcinfo = await get_lc_info(ids)
        lc_dict.update({ids : lcinfo})
        if lcinfo.get("response") == None:
            print(f"light cone with id {ids} not found")
        else:
            print(f"updating {lcinfo["data"]["name"]}")
    with open("lightCone.json", 'w', encoding='utf-8') as f:
        json.dump(lc_dict, f, ensure_ascii=False, indent=4)
        print("Successfully updated lightCone.json")

asyncio.run(update_light_cone())