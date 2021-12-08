import numpy as np
import statistics
crabs = []
with open('input.txt', 'r') as in_file:
    crabs = list(map(int, in_file.read().strip().split(',')))
npcrabs = np.array(crabs)
mean = round(statistics.mean(crabs))
best = 999999999999999999999999999
for i in range(mean-1, mean+1):
    dist = 0
    dist = sum(map(lambda n: n*(n+1)/2, abs(npcrabs - i)))
    if dist < best:
        best = dist
print(best)
