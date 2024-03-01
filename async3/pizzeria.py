
# import asyncio
# async def pizza_order(n, seconds):
#     print(f'We got pizza order {n}')
#     await asyncio.sleep(seconds)
#     print(f'Pizza {n} was cooked')
#     return f'Pizza {n} is cooked'
#
# async def main():
#     orders = [asyncio.create_task(pizza_order(n, 5-n)) for n in range(1, 5)]
#     print(await asyncio.gather(*orders))
#
# asyncio.run(main())

import asyncio
import random

class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def make_pizza(self, order_id):
        cook_time = random.randint(2, 5) # Random time to cook pizza from 2 seconds to 5
        print(f'Pizzeria {self.name} started to cook pizza for order {order_id}.')
        await asyncio.sleep(cook_time) # Waiting while pizza is cooking
        print(f'Pizzeria {self.name} finished to cook pizza for order {order_id}')

async def main():
    pizzeria = Pizzeria('Dough & Cheese')
    # creating 5 orders
    tasks = [pizzeria.make_pizza(i) for i in range(1, 6)]

    # запуск всех задач (заказов) в Event Loop
    await asyncio.gather(*tasks)

asyncio.run(main())

