import asyncio
import time

loop = asyncio.get_event_loop()

async def yo(nb):
    print(nb)
    await asyncio.sleep(1)
    await yo(nb + 1)

async def main():
    loop.create_task(yo(101))
    loop.create_task(yo(11))
    loop.create_task(yo(1))

loop.run_until_complete(main())
loop.run_forever()
loop.close()
