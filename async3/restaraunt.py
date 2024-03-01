import asyncio

async def cook_dish(n):
    print(f'Cook {n} is starting to cook')
    await asyncio.sleep(n)
    print(f'Cook {n} finished cooking')
    return f'Dish from Cook {n}'

# Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
async def main():
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)]
    print(await asyncio.gather(*tasks))

asyncio.run(main())