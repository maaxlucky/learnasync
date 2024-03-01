import asyncio

# first example of async
# async def main():
#     print('Hello...')
#     await asyncio.sleep(1)
#     print('World')
#
# asyncio.run(main())


# difference between sync and async

import time

start = time.time()


# def sleeping(n):
#     # {time.time() - start:.4f} - время от начала работы программы до текущего момента.
#     # :.4f - ограничение количества знаков после запятой (4).
#     print(f"Начало выполнения длительной операции № {n}: {time.time() - start:.4f}")
#     time.sleep(1)  # Имитация длительной операции в 1 секунду длиной.
#     print(f"Длительная операция № {n} завершена")
#
#
# def main():
#     # Запускаю 30 операций.
#     all_results = [sleeping(i) for i in range(1, 31)]
#     print(f"Выполнено {len(all_results)} операций.")
#     print(f"Программа завершена за {time.time() - start:.4f}")
#
# # Запуск главной функции.
# main()
#

async def sleeping(n):
    # {time.time() - start:.4f} - время от начала работы программы до текущего момента.
    # :.4f - ограничение количества знаков после запятой (4).
    print(f"Начало выполнения длительной операции № {n}: {time.time() - start:.4f}")
    await asyncio.sleep(1)  # Имитация длительной операции в 1 секунду длиной.
    print(f"Длительная операция № {n} завершена")


async def main():
    # Запускаю 30 операций.
    task = [sleeping(i) for i in range(1, 31)]
    all_results = await asyncio.gather(*task)
    print(f"Выполнено {len(all_results)} операций.")
    print(f"Программа завершена за {time.time() - start:.4f}")


# Запуск главной функции.
asyncio.run(main())
