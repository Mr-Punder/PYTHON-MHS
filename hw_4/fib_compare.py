import time
import threading
import multiprocessing


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def worker(n, results, i):
    results[i] = fib(n)


def sync_run(n, count):
    start = time.time()
    for _ in range(count):
        fib(n)
    return time.time() - start


def thread_run(n, count):
    start = time.time()
    results = [None] * count
    threads = [threading.Thread(target=worker, args=(n, results, i)) for i in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - start


def process_run(n, count):
    start = time.time()
    manager = multiprocessing.Manager()
    results = manager.list([None] * count)
    procs = [multiprocessing.Process(target=worker, args=(n, results, i)) for i in range(count)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    return time.time() - start


if __name__ == "__main__":
    n, count = 35, 10

    sync_t = sync_run(n, count)
    thread_t = thread_run(n, count)
    proc_t = process_run(n, count)

    with open("hw_4/results.txt", 'w') as f:
        f.write(f"fib({n}), {count} runs\n\n")
        f.write(f"sync:    {sync_t:.4f}s\n")
        f.write(f"threads: {thread_t:.4f}s (x{sync_t/thread_t:.2f})\n")
        f.write(f"process: {proc_t:.4f}s (x{sync_t/proc_t:.2f})\n")

    print(f"sync: {sync_t:.2f}s, threads: {thread_t:.2f}s, process: {proc_t:.2f}s")
