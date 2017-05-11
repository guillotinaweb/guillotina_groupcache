import asyncio
import aiohttp
import time


async def testit():
    async with aiohttp.ClientSession() as session:
        resp = await session.get('http://localhost:8080/db/container', headers={
            'Accept': 'application/json',
            'Authorization': 'Basic cm9vdDpyb290'
        })
        assert resp.status == 200


async def loaditup():
    count = 0
    start = time.time()
    while True:
        funcs = []
        for i in range(50):
            count += 1
            funcs.append(testit())
        await asyncio.gather(*funcs)
        print('{}/sec'.format(count / (time.time() - start)))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(loaditup())
