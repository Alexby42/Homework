import asyncio
import time
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        if name == 'Pasha':
            await asyncio.sleep(5)
        if name == 'Denis':
            await asyncio.sleep(4)
        if name == 'Apollon':
            await asyncio.sleep(3)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1, task2, task3
asyncio.run(start_tournament())