from aocd import get_data
import numpy as np
import time


def calculate_step(pos, vel):
    x, y = pos
    vx, vy = vel
    pos = (x+vx, y+vy)
    if vx > 0:
        vx = vx - 1
    else:
        vx = 0
    vy = vy-1
    vel = (vx, vy)
    return pos, vel


def fly(lz, start):
    min_lz = min(lz[0]), min(lz[1])
    max_lz = max(lz[0]), max(lz[1])
    vel = start
    pos = (0, 0)
    highest_y = 0
    while True:
        pos, vel = calculate_step(pos, vel)
        if pos[1] > highest_y:
            highest_y = pos[1]
        if min_lz[0] <= pos[0] <= max_lz[0] and min_lz[1] <= pos[1] <= max_lz[1]:
            return highest_y
        if pos[1] < min_lz[1] or max_lz[0] < pos[0]:
            return


def find_launch_parameters(lz):
    min_lz = min(lz[0]), min(lz[1])
    max_lz = max(lz[0]), max(lz[1])
    params = {}
    for sx in range(max_lz[0]+1):
        for sy in range(999, min_lz[1]-1, -1):
            vel = (sx, sy)
            height = fly(lz, vel)
            if height != None:
                params[vel] = height
    return params


def part1(data):
    data = data.splitlines()
    target = [list(map(int, coord[coord.index("=")+1:].split('..')))
              for coord in data[0][data[0].index(':')+2:].split(', ')]
    params = find_launch_parameters(target)
    return max(params.values())


def part2(data):
    data = data.splitlines()
    target = [list(map(int, coord[coord.index("=")+1:].split('..')))
              for coord in data[0][data[0].index(':')+2:].split(', ')]
    params = find_launch_parameters(target)
    return len(params)


data = get_data(day=17, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
