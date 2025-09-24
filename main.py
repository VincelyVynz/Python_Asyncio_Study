import time
import asyncio

async def task_1():
    print('Task 1 started')
    await asyncio.sleep(2)
    print('Task 1 completed')
    return "Task 1 Done"

async def task_2():
    print('Task 2 started')
    await asyncio.sleep(2)
    print('Task 2 completed')
    return "Task 2 Done"


async def main():
    start = time.time()
    await asyncio.gather(task_1(), task_2())
    end = time.time()
    time_elapsed = end - start
    print('Time elapsed: ' + str(time_elapsed))


if __name__ == '__main__':
    asyncio.run(main())