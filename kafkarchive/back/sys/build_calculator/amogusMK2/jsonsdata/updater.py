import json
import time
import requests
import asyncio

yattaapi = "https://sr.yatta.moe/api/v2/en/"
yattaimgapi = "https://sr.yatta.moe/hsr/assets/UI/"
hakushinapi = "https://api.hakush.in/hsr/data/"


hsrmapapi = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/en/"
hsrmapapishort = "https://raw.githubusercontent.com/FortOfFans/HSRMaps/master/"
hsrimgapi = "https://raw.githubusercontent.com/FortOfFans/HSR/main"

directory = R"img"

"""
simple updaters
"""

async def simple_pull():
    response = requests.get(f"{hakushinapi}/en/character/1005.json")
    with open("1005.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

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
    response = requests.get(f"{hakushinapi}character.json")
    id_lists = list(())
    for ids in response.json():
        id_lists.append(ids)
    return id_lists

async def get_avatar_info(id):
    response = requests.get(f"{yattaapi}avatar/{id}")
    return response.json()

async def get_hakushin_avatar_info(id):
    response = requests.get(f"{hakushinapi}/en/character/{id}.json")
    return response.json()

async def update_avatar():
    print("updating avatar.json and avatarhk.json")
    avtr_dict = dict()
    avtr_hk_dict = dict()
    id_lists = await get_all_avtr_id()
    for ids in id_lists:
        avtrinfo = await get_avatar_info(ids)
        avtrhkinfo = await get_hakushin_avatar_info(ids)
        avtr_dict.update({ids : avtrinfo})
        avtr_hk_dict.update({ids : avtrhkinfo})
        if avtrinfo.get("response") == None:
            print(f"character with id {ids} not found")
        else:
            print(f"updating {avtrinfo["data"]["name"]}")
    with open("avatar.json", 'w', encoding='utf-8') as f:
        json.dump(avtr_dict, f, ensure_ascii=False, indent=4)
        print("Successfully updated avatar.json")
    with open("avatarhk.json", 'w', encoding='utf-8') as f:
        json.dump(avtr_hk_dict, f, ensure_ascii=False, indent=4)
        print("Successfully updated avatarhk.json")

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
    response = requests.get(f"{hakushinapi}lightcone.json")
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

async def update_lcs():
    response = requests.get(f"{hsrmapapi}weapons.json")
    with open("weapons.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Successfully updated weapons.json")

        

"""
image stuff
"""

async def char_icon(id):
    response = requests.get(f"{yattaimgapi}/avatar/{id}.png")
    with open(Rf"{directory}\chars\{id}.png", 'wb') as f:
        f.write(response.content)

async def char_big(id):
    response = requests.get(f"{yattaimgapi}/avatar/large/{id}.png")
    with open(Rf"{directory}\charbig\{id}.png", 'wb') as f:
        f.write(response.content)

async def update_all_char_icons():
    id_lists = await get_all_avtr_id()
    for ids in id_lists:
        print(f"updating {ids}.png")
        await char_icon(ids)
        await char_big(ids)
    print("Successfully updated character images")

async def lc_icon(id):
    response = requests.get(f"{yattaimgapi}/equipment/medium/{id}.png")
    with open(Rf"{directory}\lightcones\{id}.png", 'wb') as f:
        f.write(response.content)

async def lc_bg(id):
    response = requests.get(f"{yattaimgapi}/equipment/large/{id}.png")
    with open(Rf"{directory}\lightconebg\{id}.png", 'wb') as f:
        f.write(response.content)

async def update_all_lc_icons():
    id_lists = await get_all_lc_id()
    for ids in id_lists:
        print(f"updating {ids}.png")
        await lc_icon(ids)
        await lc_bg(ids)
    print("Successfully updated light cone images")

async def get_all_relic_setid():
    response = requests.get(f"{hakushinapi}relicset.json")
    id_lists = list(())
    for ids in response.json():
        id_lists.append(ids)
    return id_lists

async def relic_icon(ids,relictype):
    response = requests.get(f"{yattaimgapi}/relic/IconRelic_{ids}_{relictype}.png")
    with open(Rf"{directory}\relics\IconRelic_{ids}_{relictype}.png", 'wb') as f:
        f.write(response.content)

async def check_if_relic_is_planar(id):
    response = requests.get(f"{yattaapi}relic")
    data = response.json()
    return data["data"]["items"][str(id)]["isPlanarSuit"]

async def update_all_relic_icons():
    response = await get_all_relic_setid()
    for relics in response:
        if await check_if_relic_is_planar(relics) == False:
            for relictype in range(1,5):
                await relic_icon(relics, relictype)
                print(f"updating IconRelic_{relics}_{relictype}.png")
        else: 
            for relictype in range(5,7):
                await relic_icon(relics, relictype)
                print(f"updating IconRelic_{relics}_{relictype}.png")
    print("Successfully updated relic images")


"""
please fix
get 1-4 or 5-6 from set id

"""
"""
async def alljson() -> None:
    await update_avatar()
    print("Loading...")
    time.sleep(10)
    await update_light_cone()
    print("Loading...")
    time.sleep(10)
    await update_lcs()
    print("Loading...")
    time.sleep(10)
    await update_chars()
    print("Loading...")
    time.sleep(10)
    await update_relic_main()
    print("Loading...")
    time.sleep(10)
    await update_relic_sub()
    print("Loading...")
    time.sleep(10)
    await update_relics()
    print("Loading...")
    time.sleep(10)
    await update_stats()

async def allimg() -> None:
    await update_all_relic_icons()
    print("Loading...")
    time.sleep(60)
    await update_all_lc_icons()
    print("Loading...")
    time.sleep(60)
    await update_all_char_icons()

async def hakushin_get_all_avtr_id():
    response = requests.get(f"{hakushinapi}character.json")
    id_lists = list(())
    for ids in response.json():
        id_lists.append(ids)
    print(id_lists)

"""

#asyncio.run(check_if_relic_is_planar(101))
#asyncio.run(allimg())

async def update_all_data() -> None:
    await update_avatar()
    ##await update_all_char_icons()
    #await update_all_lc_icons()
    #await update_all_relic_icons()

asyncio.run(update_all_data())
#asyncio.run(simple_pull()) 
"""
this file updates the json files
"""