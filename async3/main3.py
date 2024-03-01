# import asyncio
#
#
# async def fetch_data():
#     print('Загрузка данных...')
#     await asyncio.sleep(2)
#     return 'Данные'
#
#
# async def process_data():
#     print('Обработка данных...')
#     await asyncio.sleep(1)
#     return 'Данные обработаны'
#
#
# async def main():
#     fetched_data = await fetch_data()
#     processed_data = await process_data()
#     print(fetched_data, processed_data)
#
#
# asyncio.run(main())

import asyncio

async def download_file(url):
    # Здесь могла бы быть асинхронная операция загрузки файла
    print(f"Downloading {url}...")
    await asyncio.sleep(1) # Имитация асинхронной задержки
    print(f"Downloaded {url}!")

async def main():
    urls = ["http://example.com/file1", "http://example.com/file2"]
    await asyncio.gather(*[download_file(url) for url in urls])

asyncio.run(main())