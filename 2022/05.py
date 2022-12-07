from aocd import get_data
import numpy as np

stacks = [one, two, three, four, five, six, seven, eight, nine]


def part1(data):
    lines = data.splitlines()
    lines = lines[10:]
    for line in lines:
        line = line.split()
        num_to_move = int(line[1])
        from_stack = int(line[3])-1
        to_stack = int(line[5])-1
        moved_crates = stacks[from_stack][-num_to_move:]
        moved_crates.reverse()
        stacks[to_stack].extend(moved_crates)
        stacks[from_stack] = stacks[from_stack][:-num_to_move]
    sol = [stack[-1] for stack in stacks]
    print(sol)
    return data


def part2(data):
    lines = data.splitlines()
    lines = lines[10:]
    for line in lines:
        line = line.split()
        num_to_move = int(line[1])
        from_stack = int(line[3])-1
        to_stack = int(line[5])-1
        moved_crates = stacks[from_stack][-num_to_move:]
        stacks[to_stack].extend(moved_crates)
        stacks[from_stack] = stacks[from_stack][:-num_to_move]
    sol = [stack[-1] for stack in stacks]
    print(sol)
    return data


data = get_data(day=5, year=2022)
'''THIS DAY ONLY WORKS ONE PART AT A TIME DUE TO GLOBAL VARIABLES
    STACKS ARE NOT RESET BETWEEN PARTS
    STACKS NEED TO BE MANUALY GRABBED FROM THE WEBSITE
'''
# part1(data)

part2(data)
