from aocd import get_data
import numpy as np
import statistics
from collections import Counter
import time


def part1(data):
    data = data.splitlines()

    polys = data[:data.index('')][0]
    rules = data[data.index('')+1:]
    rules = dict([rule.split(' -> ') for rule in rules])

    for i in range(10):
        new_polys = [polys[0]]
        for first, second in zip(polys, polys[1:]):
            if first+second in rules:
                new_polys.append(rules[first+second])
                new_polys.append(second)

        polys = new_polys
    counter = Counter(polys)
    common = counter.most_common()
    return common[0][1] - common[-1][1]


def part2(data):
    data = data.splitlines()

    polys = data[:data.index('')][0]
    polys = [first+second for first, second in zip(polys, polys[1:])]
    counts = {}

    rules = data[data.index('')+1:]
    rules = dict([rule.split(' -> ') for rule in rules])
    elements = dict.fromkeys(rules.values(), 0)

    for key, value in rules.items():
        rules[key] = [key[0]+value, value+key[1]]
        counts[key] = 0
        counts[key[0]+value] = 0
        counts[value+key[1]] = 0
    for poly in polys:
        counts[poly] += 1
    for i in range(40):
        temp = counts.copy()
        for key, number in counts.items():
            if number:
                for rule in rules[key]:
                    temp[rule] += number
                temp[key] -= number
        counts = temp.copy()
    for key, number in counts.items():
        for element in elements.keys():
            if element == key[1]:
                elements[element] += number

    num_elems = list(elements.values())
    num_elems.sort()

    return num_elems[-1] - num_elems[0]


data = get_data(day=14, year=2021)
start = time.perf_counter_ns()
print(part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

print(part2(data))

times = []
for i in range(100_000):
    if i % 10_000 == 0:
        print(i)

    start = time.perf_counter_ns()
    part2(data)
    end = time.perf_counter_ns()
    mes = (end-start)/1e+6
    times.append(mes)
print(f'Mean: {statistics.mean(times)}ms')
print(f'Median: {statistics.median(times)}ms')
