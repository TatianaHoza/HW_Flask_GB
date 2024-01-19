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
folder = 'data_task'
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

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
for process in processes:
    process.join()

print(f"Downloaded {urls} in {time.time() - start_time:.2f} seconds")

async def download_as(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            file = os.path.join(folder, url.split('/')[-1])
            with open(file, "w", encoding='utf-8') as f:
                f.write(text)


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_as(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print(f"Downloaded {urls} in {time.time() - start_time:.2f} seconds")