import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_part(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_class=ThreadPoolExecutor):
    if n_jobs == 1:
        return integrate_part(f, a, b, n_iter)

    chunk_size = n_iter // n_jobs
    tasks = []
    for i in range(n_jobs):
        start = a + i * (b - a) / n_jobs
        end = a + (i + 1) * (b - a) / n_jobs
        tasks.append((f, start, end, chunk_size))

    with executor_class(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_part, *task) for task in tasks]
        results = [f.result() for f in futures]

    return sum(results)


def benchmark():
    cpu_count = os.cpu_count()
    results = []

    for n_jobs in range(1, cpu_count * 2 + 1):
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_class=ThreadPoolExecutor)
        thread_time = time.time() - start

        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_class=ProcessPoolExecutor)
        process_time = time.time() - start

        results.append((n_jobs, thread_time, process_time))
        print(f"n_jobs={n_jobs:2d}: threads={thread_time:.4f}s, process={process_time:.4f}s")

    return results


if __name__ == "__main__":
    results = benchmark()

    with open("hw_4/artifacts/integrate_results.txt", 'w') as f:
        f.write("n_jobs  threads(s)  process(s)\n")
        f.write("-" * 35 + "\n")
        for n_jobs, thread_time, process_time in results:
            f.write(f"{n_jobs:4d}    {thread_time:8.4f}    {process_time:8.4f}\n")
