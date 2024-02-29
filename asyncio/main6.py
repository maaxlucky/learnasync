import asyncio

# иммитация асинхроного соединения с некой периферией
async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('Sending data...')
            await asyncio.sleep(2)
            print('Data was sent')

        async def get_data(self):
            print('getting data...')
            await asyncio.sleep(2)
            print('data have got')

        async def close(self):
            print('finishing connection...')
            await asyncio.sleep(2)
            print('connection finished.')


    print('Establishing connection...')
    await asyncio.sleep(2)
    print('connection established.')
    return Conn()

class Connection:
    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операции отправки и получения данных выполняем конкурентно
        await send_task
        await receive_task


asyncio.run(main())
