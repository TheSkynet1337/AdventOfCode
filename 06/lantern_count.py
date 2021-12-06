import numpy as np
import time
fishes = []
with open('input.txt', 'r') as in_file:
    fishes = list(map(int, in_file.read().strip().split(',')))
days = 256
counters = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i, f in enumerate(fishes):
    counters[f] += 1
pre_counters = counters[:]
times = []
for x in range(1_000_001):
    oldzero = 0
    start = time.perf_counter_ns()
    for d in range(days):
        for f in range(9):
            if f == 8:
                counters[8] = oldzero
                counters[6] += oldzero
                continue
            if f == 0:
                oldzero = counters[0]
            counters[f] = counters[f+1]
    end = time.perf_counter_ns()
    times.append(end-start)
    if x % 100_000 == 0:
        print(x)
    counters = pre_counters[:]
print(f'mean: {sum(times)/len(times)} nanoseconds')
times.sort()
print(f'median: {times[round(len(times)/2)]} nanoseconds')
print(sum(counters))
