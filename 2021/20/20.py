from aocd import get_data
import time
import numpy as np
from anytree import Node, RenderTree, PreOrderIter
import math
import json
from itertools import combinations


def part1(data):
    data = data.replace('#', '1')
    data = data.replace('.', '0')
    f, img = data.split('\n\n')
    img = img.splitlines()

    rows = [r for r in img]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    img = np.array(int_rows)
    f = list(f)
    print(img)
    f = [int(c) for c in f]
    # print(f)
    iterations = 50
    # print(img)
    img = np.pad(img, 3*iterations)
    old_shape = img.shape
    for i in range(iterations):
        output = []
        print(old_shape)
        print(img.shape)
        window_matrix = np.lib.stride_tricks.sliding_window_view(img, (3, 3))
        stride = 1
        for window_list in window_matrix:
            for window in window_list:
                if stride == 1:
                    # print(window)
                    stride = 0
                num_str = ''.join([str(elem)
                                   for sublist in window for elem in sublist])
                # print(num_str)
                num = int(num_str, 2)
                # print(num)
                # print(f[num])
                output.append(f[num])
        img = np.reshape(output, (-1, int(math.sqrt(len(output)))))
        print(img)
    # print(output)
    # print(len(output))

    return sum(sum(img))


def part2(data):
    data = data.splitlines()

    return


data = get_data(day=20, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
