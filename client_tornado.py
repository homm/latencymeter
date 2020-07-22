import sys
import time
import asyncio
import uvloop
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

uvloop.install()
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

url = sys.argv[1]
times = int(sys.argv[2])

async def run():
    http_client = AsyncHTTPClient()
    start = time.time()
    for _ in range(times):
        resp = await http_client.fetch(url)
        assert resp.body == b'hello world'
    return time.time() - start


elapsed = IOLoop.current().run_sync(run)
print('average: {:0.3f}ms'.format(elapsed / times * 1000))
