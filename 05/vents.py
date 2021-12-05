import numpy as np
from operator import methodcaller


def mark_coords(pair1, pair2):
    for i in range(pair1[0], pair2[0]):
        diagram[i][pair1[1]] += 1
    for i in range(pair1[1], pair2[1]):
        diagram[pair1[0]][i] += 1
    diagram[pair2[0]][pair2[1]] += 1


lines = []

with open('test.txt', 'r') as in_file:
    lines = in_file.read().splitlines()

diagram = np.zeros((1000, 1000))

split_lines = []
for line in lines:
    split_line = line.split(' -> ')
    split_lines.append(split_line)
    # print(split_line)
    start = list(map(int, split_line[0].split(',')))
    end = list(map(int, split_line[1].split(',')))
    print(start, end)
    if start[0] == end[0]:
        if start[1] < end[1]:
            mark_coords(start, end)
        else:
            mark_coords(end, start)
    elif start[1] == end[1]:
        if start[0] < end[0]:
            mark_coords(start, end)
        else:
            mark_coords(end, start)
print(diagram)
print((diagram > 1).sum())
