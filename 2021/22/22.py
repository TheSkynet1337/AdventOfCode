from aocd import get_data
import time
import numpy as np
from anytree import Node, RenderTree, PreOrderIter
import math
import json
from itertools import combinations
from functools import cache
from scipy.sparse import dok_matrix
from collections import Counter
import re


def part1(data):
    data = data.splitlines()
    # data = [
    #     'on x=-20..26,y=-36..17,z=-47..7',
    #     'on x=-20..33,y=-21..23,z=-26..28',
    #     'on x=-22..28,y=-29..23,z=-38..16',
    #     'on x=-46..7,y=-6..46,z=-50..-1',
    #     'on x=-49..1,y=-3..46,z=-24..28',
    #     'on x=2..47,y=-22..22,z=-23..27',
    #     'on x=-27..23,y=-28..26,z=-21..29',
    #     'on x=-39..5,y=-6..47,z=-3..44',
    #     'on x=-30..21,y=-8..43,z=-13..34',
    #     'on x=-22..26,y=-27..20,z=-29..19',
    #     'off x=-48..-32,y=26..41,z=-47..-37',
    #     'on x=-12..35,y=6..50,z=-50..-2',
    #     'off x=-48..-32,y=-32..-16,z=-15..-5',
    #     'on x=-18..26,y=-33..15,z=-7..46',
    #     'off x=-40..-22,y=-38..-28,z=23..41',
    #     'on x=-16..35,y=-41..10,z=-47..6',
    #     'off x=-32..-23,y=11..30,z=-14..3',
    #     'on x=-49..-5,y=-3..45,z=-29..18',
    #     'off x=18..30,y=-20..-8,z=-3..13',
    #     'on x=-41..9,y=-7..43,z=-33..15',
    #     'on x=-54112..-39298,y=-85059..-49293,z=-27449..7877',
    #     'on x=967..23432,y=45373..81175,z=27513..53682'
    # ]
    # data = [
    #     'on x=10..12,y=10..12,z=10..12',
    #     'on x=11..13,y=11..13,z=11..13',
    #     'off x=-9..-11,y=-9..-11,z=-9..11',
    #     'on x=10..10,y=10..10,z=10..10'
    # ]
    data = [line.split(' ') for line in data]
    command = [line[0] for line in data]
    data = [line[1] for line in data]
    data = [line[line.index('x='):].split(',') for line in data]
    coordinates = []
    for coords in data:
        xyz = []
        for coord in coords:
            xyz.append(list(map(lambda x: x+50, filter(lambda x: -50 <= x <= 50,
                       map(int, coord[coord.index("=")+1:].split('..'))))))
        coordinates.append(xyz)
    reactor = np.zeros((101, 101, 101), dtype=bool)
    for i, group in enumerate(coordinates):
        if group[0]:
            xmin = group[0][0]
            xmax = group[0][1]+1
            ymin = group[1][0]
            ymax = group[1][1]+1
            zmin = group[2][0]
            zmax = group[2][1]+1
            reactor[xmin:xmax, ymin:ymax, zmin:zmax] = command[i] == 'on'
    # print(reactor[10:13, 10:13, 10:13].size)
    return np.count_nonzero(reactor)


def part2(data):
    # i stole this from https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpizza8/?utm_source=share&utm_medium=web2x&context=3
    # sry
    data = data.splitlines()
    cubes = Counter()
    for line in data:
        new_sign = 1 if line.split(' ')[0] == 'on' else -1
        new_x0, new_x1, new_y0, new_y1, new_z0, new_z1 = map(
            int, re.findall('-?\d+', line))
        # keep track of changes made by this input line
        update = Counter()
        # find out if new cube is inside existing cubes
        for (existing_x0, existing_x1, existing_y0, existing_y1, existing_z0, existing_z1), existing_sign in cubes.items():
            inside_x0 = max(new_x0, existing_x0)
            inside_x1 = min(new_x1, existing_x1)
            inside_y0 = max(new_y0, existing_y0)
            inside_y1 = min(new_y1, existing_y1)
            inside_z0 = max(new_z0, existing_z0)
            inside_z1 = min(new_z1, existing_z1)
            # if so set existing cube to not matter in later counting by setting its sign to 0
            if inside_x0 <= inside_x1 and inside_y0 <= inside_y1 and inside_z0 <= inside_z1:
                update[(inside_x0, inside_x1, inside_y0, inside_y1,
                        inside_z0, inside_z1)] -= existing_sign
        # if new cube is 'on' turn cube on and add to update
        if new_sign > 0:
            update[(new_x0, new_x1, new_y0, new_y1,
                    new_z0, new_z1)] += new_sign
        # add updates to all cubes(these are 'inside' cubes set to 0 and the new cube set to new_sign)
        cubes.update(update)
    # count on coordinates by taking x*y*z*sign for each cube, cubes set to 0 are ignored off cubes are subtracted and on cubes added
    return sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
               for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())


data = get_data(day=22, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
