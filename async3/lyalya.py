import asyncio


async def callee():
    return input('Введи слово уже...')

async def caller():
    # loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(callee())
    result = await future
    # very interesting usecase with lambd
    future.add_done_callback(lambda f: print(f.result() + ' World'))
    while not future.done():
        pass
        # print('lya lya lya lay')
    # print(result + ' World')


async def main():
   await asyncio.create_task(caller())


asyncio.run(main())


