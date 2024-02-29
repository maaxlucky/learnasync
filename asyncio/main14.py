import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


# числодробилка
def cpu_bounded():
    for i in range(10000000):
        _ = i ** 3


async def main(n):
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, cpu_bounded) for _ in range(n)]

        await asyncio.gather(*tasks)

# варьируйте n от 1 до 10 и проследите за временем выполнением программы
n = 10

print(time.strftime('%X'))

asyncio.run(main(n))

print(time.strftime('%X'))

