scan = []
with open('input.txt', 'r') as in_file:
    for line in in_file.readlines():
        scan.append(int(line))

num_increases = 0

for i, depth in enumerate(scan):
    if i < 1:
        continue
    if scan[i-1] < depth:
        num_increases += 1

print(num_increases)
