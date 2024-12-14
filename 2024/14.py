import operator
import re
from functools import reduce

input = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''
area_size = (11, 7)
input = open('14.txt', 'r').read()
area_size = (101, 103)
input = input.split('\n')[:-1]
guards = [((int(x), int(y)), (int(vx), int(vy)))
          for x, y, vx, vy in [re.findall(r'-*\d+', line) for line in input]]


def visualize_field(area_size, new_guards):
    area = []
    for y in range(area_size[1]):
        area.append(''.join('.'*area_size[0]))
    for guard in new_guards:
        x, y = guard[0]
        area[y] = area[y][:x] + '#' + area[y][x+1:]
    for line in area:
        print(line)


def check_for_continuous(row):
    row = sorted([x for x, y in row])
    return sum(a+1 == b for a, b in zip(row, row[1:]))


orig_rows = []
for y in range(area_size[1]):
    orig_rows.append(set())
iters = 10000
max_len = 0
for i in range(iters):
    if i % 10000 == 0:
        print(i)
    new_guards = []
    rows = []
    for y in range(area_size[1]):
        rows.append(set())
    for guard in guards:
        x, y = guard[0]
        vx, vy = guard[1]
        new_xy = ((x+vx) % area_size[0], (y+vy) % area_size[1])
        new_guards.append((new_xy, guard[1]))
        rows[new_xy[1]].add(new_xy)
    for row in rows:
        cont = check_for_continuous(row)
        if cont > max_len:
            max_len = cont
            row = sorted([x for x, y in row])
            print('christmas tree at?', i+1)
            visualize_field(area_size, new_guards)
    guards = new_guards

quads = {'tl': 0, 'tr': 0, 'bl': 0, 'br': 0}
for guard in guards:
    x, y = guard[0]
    if x < area_size[0]//2:
        if y < area_size[1]//2:
            quads['tl'] += 1
        elif y > area_size[1]//2:
            quads['bl'] += 1
    elif x > area_size[0]//2:
        if y < area_size[1]//2:
            quads['tr'] += 1
        elif y > area_size[1]//2:
            quads['br'] += 1
print('Part 1:', reduce(operator.mul, quads.values()))
