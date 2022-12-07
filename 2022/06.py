from aocd import get_data
import numpy as np
from collections import Counter


def part1(data):
    seen = []
    for i, letter in enumerate(data):
        seen.append(letter)
        if i > 3:
            seen.pop(0)
            freq = Counter(seen)
            if len(freq) == len(seen):
                print(seen)
                print(i+1)
                break

    return data


def part2(data):
    seen = []
    for i, letter in enumerate(data):
        seen.append(letter)
        if i > 13:
            seen.pop(0)
            freq = Counter(seen)
            if len(freq) == len(seen):
                print(seen)
                print(i+1)
                break

    return data


data = get_data(day=6, year=2022)
part1(data)

part2(data)
