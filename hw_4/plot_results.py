import matplotlib.pyplot as plt

n_jobs = []
threads = []
processes = []

with open("hw_4/artifacts/integrate_results.txt", 'r') as f:
    f.readline()
    f.readline()
    for line in f:
        if line.strip():
            parts = line.split()
            n_jobs.append(int(parts[0]))
            threads.append(float(parts[1]))
            processes.append(float(parts[2]))

plt.figure(figsize=(10, 6))
plt.plot(n_jobs, threads, 'o-', label='ThreadPoolExecutor')
plt.plot(n_jobs, processes, 's-', label='ProcessPoolExecutor')
plt.xlabel('n_jobs')
plt.ylabel('Time (s)')
plt.title('Integration performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('hw_4/artifacts/plot.png', dpi=100, bbox_inches='tight')
