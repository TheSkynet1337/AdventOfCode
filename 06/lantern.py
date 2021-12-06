import numpy as np

fishes = []
with open('input.txt', 'r') as in_file:
    fishes = list(map(int, in_file.read().strip().split(',')))
days = 80
for d in range(days):
    if d % 7 == 0:
        print('d', d)
        print(len(fishes))
    pre_day_len = len(fishes)
    for f in range(pre_day_len-1, -1, -1):
        if fishes[f] == 0:
            fishes.append(8)
            fishes[f] = 6
        else:
            fishes[f] -= 1
print(fishes)
print(len(fishes))
