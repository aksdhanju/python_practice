import asyncio
import time
from multiprocessing import Process, Queue, cpu_count

HOST = "localhost"
PORT = 4221

REQUESTS_PER_PROCESS = 2000
CONCURRENCY_PER_PROCESS = 200
PROCESSES = 4   # You can set this to cpu_count()

async def send_request(i):
    reader, writer = await asyncio.open_connection(HOST, PORT)
    req = f"GET /echo/load{i} HTTP/1.1\r\n\r\n"
    writer.write(req.encode())
    await writer.drain()
    await reader.read(1024)
    writer.close()
    await writer.wait_closed()


async def worker():
    tasks = [
        asyncio.create_task(send_request(i))
        for i in range(CONCURRENCY_PER_PROCESS)
    ]
    await asyncio.gather(*tasks)


async def run_load():
    batches = REQUESTS_PER_PROCESS // CONCURRENCY_PER_PROCESS
    for _ in range(batches):
        await worker()


def process_target(result_queue):
    start = time.time()
    asyncio.run(run_load())
    end = time.time()

    result_queue.put(end - start)


def main():
    result_queue = Queue()
    processes = []

    print(f"Starting {PROCESSES} processes...")
    print(f"Each process: {REQUESTS_PER_PROCESS} requests, concurrency={CONCURRENCY_PER_PROCESS}")

    # Spawn processes
    for _ in range(PROCESSES):
        p = Process(target=process_target, args=(result_queue,))
        processes.append(p)
        p.start()

    # Wait for them to finish
    for p in processes:
        p.join()

    # Collect results
    times = [result_queue.get() for _ in range(PROCESSES)]
    total_requests = PROCESSES * REQUESTS_PER_PROCESS

    print("\n=== Load Test Complete ===")
    print(f"Total processes: {PROCESSES}")
    print(f"Total requests: {total_requests}")
    print(f"Avg time per process: {sum(times)/len(times):.2f}s")
    print(f"Requests per second: {total_requests / max(times):.2f}")


if __name__ == "__main__":
    main()
