from aocd import get_data
import time
import numpy as np
from anytree import Node, RenderTree, PreOrderIter
import math
import json
from itertools import combinations
from functools import cache


@cache
def play_quantum_game(p1, p2, s1, s2):
    wins = (0, 0)
    if s1 >= 21:
        return (1, 0)
    elif s2 >= 21:
        return (0, 1)

    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                position = (i+j+k+p1) % 10 or 10
                s1_prime = s1 + position
                q = play_quantum_game(p2, position, s2, s1_prime)
                wins = (wins[0]+q[1], wins[1]+q[0])
    return wins


def part1(data):
    data = data.splitlines()
    data = [int(line.split(': ')[1]) for line in data]
    print('start', data)
    positions = data
    scores = [0, 0]
    dice = 0
    rolls = 0
    while max(scores) <= 1000:
        movements = [0, 0]
        for _ in range(3):
            rolls += 1
            if dice >= 100:
                dice = 0
            dice += 1
            movements[0] += dice

        positions[0] = (movements[0] + positions[0]) % 10 or 10

        scores[0] += positions[0]+1
        if scores[0] >= 1000:
            break
        for _ in range(3):
            rolls += 1
            if dice >= 100:
                dice = 0
            dice += 1
            movements[1] += dice
        positions[1] = (movements[1] + positions[1]) % 10 or 10

        scores[1] += positions[1]+1

    loser_score = min(scores)
    return loser_score * rolls


def part2(data):
    data = data.splitlines()
    data = [int(line.split(': ')[1]) for line in data]
    print('start', data)
    positions = data

    wins = play_quantum_game(positions[0], positions[1], 0, 0)
    return max(wins)


data = get_data(day=21, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
