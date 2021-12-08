import numpy as np

scan = []
with open('input.txt', 'r') as in_file:
    for line in in_file.readlines():
        scan.append(int(line))

num_increases = 0

scan = np.array(scan)
windows = np.lib.stride_tricks.sliding_window_view(scan, 3)
for i, window in enumerate(windows):
    if i < 1:
        continue
    if np.sum(windows[i-1]) < np.sum(window):
        num_increases += 1

print(num_increases)
