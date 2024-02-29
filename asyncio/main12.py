import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    # используем низкоуровневые функции цикла событий
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'We got request for connection from {address}')
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # извлекаем цикл событий
    asyncio_loop = asyncio.get_event_loop()

    await listen_for_connection(server_socket, asyncio_loop)


asyncio.run(main())
