import yatta
import asyncio
import json

async def main() -> None:
    async with yatta.YattaAPI(headers={"Kiryuuin":"testing for a school project website"}) as client:
        fetched = await client.fetch_character_detail(1005)
        #print(fetched.traces)
        traceval = {}
        for yattatrace in fetched.traces.sub_skills:
            #print(yattatrace.name)
            #print(yattatrace.id)
            for stats in yattatrace.status_list:
                traceval.update({yattatrace.id:stats.value})
                #print(stats.value)

        print(json.dumps(traceval, indent=4, sort_keys=False))

asyncio.run(main())