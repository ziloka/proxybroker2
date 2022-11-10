"""Find 10 working HTTP(S) proxies and save them to a file."""

import asyncio

from proxybroker import Broker


async def save(proxies, filename):
    """Save proxies to a file."""
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = f'{proto}://{proxy.host}:{proxy.port}\n'
            f.write(row)


async def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    await asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit=10),
        save(proxies, filename='proxies.txt'),
    )



if __name__ == '__main__':
    loop = asyncio.get_event_loop_policy().get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
