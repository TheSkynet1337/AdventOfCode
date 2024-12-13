import re

import numpy as np
from tqdm import tqdm

input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
input = open("13.txt", "r").read()
input = input.split("\n\n")
machines = []
for machine in input:
    machines.append([int(num) for num in re.findall(r"\d+", machine)])
tokens = 0
for machine in machines:
    for a in range(101):
        for b in range(101):
            x = a * machine[0] + b * machine[2]
            y = a * machine[1] + b * machine[3]
            if x == machine[4] and y == machine[5]:
                tokens += a * 3 + b
print("Part 1:", tokens)
pt2tokens = 0


ok = []
for machine in machines:
    coefficients = np.array([[machine[0], machine[2]], [machine[1], machine[3]]])
    targets = np.array([machine[4], machine[5]]) + 10000000000000
    res = np.linalg.solve(coefficients, targets).round()
    if all(coefficients @ res == targets):
        ok.append(res[0] * 3 + res[1])
print("Part 2:", int(sum(ok)))
