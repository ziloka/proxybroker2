"""Find and show 10 working HTTP(S) proxies."""

import asyncio

from proxybroker import Broker


async def main():
    async def show(proxies):
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            print(f'Found proxy: {proxy}')


    proxies = asyncio.Queue()
    broker = Broker(proxies, loop=asyncio.get_running_loop())

    await asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit=10), show(proxies))

loop = asyncio.get_event_loop_policy().get_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
