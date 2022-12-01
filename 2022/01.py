from aocd import get_data
import numpy as np


def part1(data):
    elves = data.split('\n\n')
    elves = [e.splitlines() for e in elves]
    cur_max = 0
    for elf in elves:
        elf = map(int, elf)
        cur_max = max(cur_max, sum(elf))
    print(cur_max)
    return data


def part2(data):
    elves = data.split('\n\n')
    elves = [e.splitlines() for e in elves]
    calories_list = []
    for elf in elves:
        elf = map(int, elf)
        calories_list.append(sum(elf))
    print(sum(sorted(calories_list)[-3:]))
    return data


data = get_data(day=1, year=2022)
part1(data)
part2(data)
