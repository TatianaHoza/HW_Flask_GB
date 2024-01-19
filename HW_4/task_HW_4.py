'''Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.'''

import requests
import time
import os
import threading
from multiprocessing import Process
import asyncio
import aiohttp

urls = ['https://cdn.pixabay.com/photo/2024/01/07/14/12/man-8493244_1280.jpg',
        'https://cdn.pixabay.com/photo/2023/09/13/13/48/cactus-8250996_1280.jpg',
        'https://cdn.pixabay.com/photo/2023/10/17/03/23/child-8320341_1280.png'
        ]
start_time = time.time()
folder = 'data_HW'
if not os.path.exists(folder):
    os.mkdir(folder)


def download(url):
    response = requests.get(url)
    file = os.path.join(folder, url.split('/')[-1])
    with open(file, "w", encoding='utf-8') as f:
        f.write(response.text)


threads = []
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

processes = []


async def download_as(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.content.read()
            file = os.path.join(folder, url.split('/')[-1])
            with open(file, "w", encoding='utf-8') as f:
                f.write(text)


if __name__ == '__main__':
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_as(url))
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
print(f"Downloaded {urls} in {time.time() - start_time:.2f} seconds")

processes = []
for url in urls:
    process = Process(target=download, args=(url,))
    processes.append(process)
    process.start()
    for process in processes:
        process.join()
print(f"Downloaded {urls} in {time.time() - start_time:.2f} seconds")
