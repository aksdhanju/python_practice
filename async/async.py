import asyncio

# Blocking example
import time
for i in range(5):
    print(f"\rLoading {i}", end="")
    time.sleep(1) # thread blocked

print('\nNow async sleep')
# Async example

async def main():
    for i in range(5):
        print(f"\rLoading {i}", end="")
        await asyncio.sleep(1) # only coroutine blocked

asyncio.run(main())
print('\n async sleep done')


async def main():
    for i in range(5):
        print(f"Task {i} starting")
        await asyncio.sleep(1)  # waits sequentially
        print(f"Task {i} done")

asyncio.run(main())


async def worker(i):
    print(f"Task {i} starting")
    await asyncio.sleep(1)   # non-blocking
    print(f"Task {i} done")

async def main_only_gather():
    # tasks = [worker(i) for i in range(5)]
    tasks = []
    for i in range(5):
        tasks.append(worker(i))
    # await asyncio.gather(*tasks)  # run in parallel
    await asyncio.gather(tasks[0],tasks[1],tasks[2],tasks[3],tasks[4])

asyncio.run(main_only_gather())


async def main_create_task():
    # tasks = [asyncio.create_task(worker(i)) for i in range(5)]
    tasks = []                      # start with an empty list
    for i in range(5):              # loop over 0,1,2,3,4
        t = asyncio.create_task(worker(i))   # schedule worker(i) as a Task
        tasks.append(t)             # add the Task object to the list
    print("All tasks started!")
    await asyncio.sleep(0.5)
    print("Still waiting, but tasks are working in background...")
    await asyncio.gather(*tasks)

asyncio.run(main_create_task())