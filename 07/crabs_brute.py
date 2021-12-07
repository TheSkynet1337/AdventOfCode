
crabs = []
with open('input.txt', 'r') as in_file:
    crabs = list(map(int, in_file.read().strip().split(',')))

best = 999999999999999999999999999
for i in range(-1, max(crabs)):
    dist = 0
    for crab in crabs:
        n = abs(crab - i)
        dist += n * (n + 1) / 2
    if dist < best:
        best = dist
print(best)
