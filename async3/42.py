import asyncio

async def async_func():
    def sync_func():

        # Тут может быть любой синхронный код
        return 42

    result = sync_func()
    print(result)

asyncio.run(async_func())

import asyncio
import time

start = time.time()
async def first():
    print('Запуск задачи first')
    print('начало 5 сек подсчета')
    time.sleep(5)
    print('5 сек подсчет завершен')
    print('начало 30 сек запроса в БД')
    await asyncio.sleep(30)
    print('30 сек запрос в БД завершен')
    print('начало 10 сек подсчета каких-то агрегатов')
    time.sleep(10)
    print('10 сек подсчета каких-то агрегатов завершено')
    print('Задача first завершена')

async def second():
    print('Запуск задачи second')
    print('начало 1 мин обучение нейронки')
    time.sleep(60)
    print('1 мин обучение нейронки завершено')
    print('Задача second завершена')

async def third():
    print('Запуск задачи third')
    await asyncio.sleep(1)
    print('начало 20 сек построение прогноза')
    print('20 сек построение прогноза завершено')
    print('Задача third завершена')

async def main():
    await asyncio.gather(first(), second(), third())

asyncio.run(main())
print(time.time() - start)