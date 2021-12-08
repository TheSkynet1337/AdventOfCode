import numpy as np
from operator import methodcaller

lines = []
numbers = []
bingo_fields = []
with open('input.txt', 'r') as in_file:
    lines = list(filter(None, in_file.read().splitlines()))

numbers = list(map(int, lines.pop(0).split(',')))
for chunk in [lines[i:i+5] for i in range(0, len(lines), 5)]:
    bingo_fields.append(np.array(
        [list(map(int, filter(None, row))) for row in map(methodcaller('split', ' '), chunk)]))
hits = []
for field in bingo_fields:
    hits.append(np.full(field.shape, False))

for number in numbers:
    for i, field in enumerate(bingo_fields):
        cur_hits = field == number
        hits[i] = np.array(np.logical_or(cur_hits, hits[i]))
        if np.all(hits[i], axis=0).any() or np.all(hits[i], axis=1).any():
            unmarked_sum = np.sum(np.ma.array(field, mask=hits[i]))
            print('part1', unmarked_sum*number)
            break
    else:
        continue
    break

wins = [False for _ in hits]

for number in numbers:
    for i, field in enumerate(bingo_fields):
        cur_hits = field == number
        hits[i] = np.array(np.logical_or(cur_hits, hits[i]))
        # print(wins)
        wins[i] = np.all(hits[i], axis=0).any(
        ) or np.all(hits[i], axis=1).any()
        if all(wins):
            unmarked_sum = np.sum(np.ma.array(field, mask=hits[i]))
            print('part2', unmarked_sum*number)
            break
    else:
        continue
    break
