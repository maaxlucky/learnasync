import asyncio
import functools
import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

    weather_json = requests.get(url=url, params=params).json()
    print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    # извлекаем цикл событий
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        # раскладываем задачи по отдельным потокам
        tasks = [loop.run_in_executor(pool, functools.partial(get_weather, city)) for city in cities_]

        await asyncio.gather(*tasks)


print(time.strftime('%X'))

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

asyncio.run(main(cities))

print(time.strftime('%X'))