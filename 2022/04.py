from aocd import get_data
import numpy as np


def part1(data):
    pairs = data.splitlines()
    pairs = [pair.split(",") for pair in pairs]
    overlaps = 0
    for pair in pairs:
        elf1 = [int(n) for n in pair[0].split("-")]
        elf2 = [int(n) for n in pair[1].split("-")]
        if elf1[0] == elf2[0] and elf1[1] == elf2[1]:
            overlaps += 1
        elif elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            overlaps += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            overlaps += 1

    print(overlaps)
    return data


def part2(data):
    pairs = data.splitlines()
    pairs = [pair.split(",") for pair in pairs]
    overlaps = 0
    for pair in pairs:
        elf1 = [int(n) for n in pair[0].split("-")]
        elf2 = [int(n) for n in pair[1].split("-")]
        if elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
            overlaps += 1
        elif elf1[0] <= elf2[1] and elf1[0] >= elf2[0]:
            overlaps += 1
        elif elf1[0] == elf2[0] and elf1[1] == elf2[1]:
            overlaps += 1
        elif elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            overlaps += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            overlaps += 1
    print(overlaps)
    return data


data = get_data(day=4, year=2022)
part1(data)

part2(data)
