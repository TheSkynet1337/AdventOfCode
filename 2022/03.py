from aocd import get_data
import numpy as np


def part1(data):
    bags = data.splitlines()
    split_bags = []
    for bag in bags:
        first = bag[:len(bag)//2]
        second = bag[len(bag)//2:]
        split_bags.append([first, second])
    priorities = []
    for bag in split_bags:
        common = list(set(bag[0]).intersection(set(bag[1])))[0]
        # priorities.append(common)
        if common.isupper():
            priorities.append(ord(common)-38)
        else:
            priorities.append(ord(common)-96)
    print(sum(priorities))
    return data


def part2(data):
    bags = data.splitlines()
    priorities = []
    for n in range(0, len(bags), 3):
        bag1 = bags[n]
        bag2 = bags[n+1]
        bag3 = bags[n+2]
        common = list(set(bag1).intersection(set(bag2), set(bag3)))[0]
        if common.isupper():
            priorities.append(ord(common)-38)
        else:
            priorities.append(ord(common)-96)
    print(sum(priorities))

    return data


data = get_data(day=3, year=2022)
part1(data)

part2(data)
