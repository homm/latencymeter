import sys
import time
import asyncio
import uvloop
import aiohttp

uvloop.install()

url = sys.argv[1]
times = int(sys.argv[2])

async def run():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        for _ in range(times):
            resp = await session.get(url)
            body = await resp.read()
            assert body == b'hello world'
        return time.time() - start


elapsed = asyncio.get_event_loop().run_until_complete(run())
print('average: {:0.3f}ms'.format(elapsed / times * 1000))
