import asyncio

async def get_message():
    await asyncio.create_task(asyncio.sleep(2)) # иммитация ожидания сообщения от клиента
    print('Hi server!')


async def listen_post():
    while True:
        await asyncio.sleep(5) # имитация ожидания запроса на соединение от клиента
        print('Получен запрос на соединение, ждем сообщения')
        asyncio.create_task(get_message())


async def main():
    await asyncio.create_task(listen_post())


asyncio.run(main())
