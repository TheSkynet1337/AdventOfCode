import numpy as np
import statistics

crabs = []
with open('input.txt', 'r') as in_file:
    crabs = list(map(int, in_file.read().strip().split(',')))
npcrabs = np.array(crabs)
target = statistics.median(crabs)

print(sum(abs(npcrabs - target)))
