from aocd import get_data
import numpy as np
import math


def part1(data):
    # data = [
    #     '2199943210',
    #     '3987894921',
    #     '9856789892',
    #     '8767896789',
    #     '9899965678',
    # ]
    data = data.splitlines()
    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    heights = np.array(int_rows)
    pad_heights = np.pad(heights, 1, mode='constant', constant_values=9)
    is_lowest = np.zeros(heights.shape, dtype=bool)
    # rows =
    for ix, iy in np.ndindex(heights.shape):
        if pad_heights[ix][iy+1] > heights[ix][iy] and pad_heights[ix+1][iy] > heights[ix][iy] and pad_heights[ix+2][iy+1] > heights[ix][iy] and pad_heights[ix+1][iy+2] > heights[ix][iy]:
            is_lowest[ix][iy] = True

    return np.sum(np.ma.array(heights+1, mask=np.invert(is_lowest)))


def find_basin_size(M, x, y):
    pad_M = np.pad(M, 1)
    print(pad_M)
    for ix, iy in np.ndindex(M.shape):
        break
    return


def part2(data):
    data = data.splitlines()
    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    heights = np.array(int_rows)
    basins = heights < 9
    m, n = basins.shape
    islands = {(r, c): {(r, c)} for r in range(m)
               for c in range(n) if basins[r][c]}
    for (r, c) in list(islands):
        for nr, nc in [(r+1, c), (r, c+1)]:
            if(nr, nc) not in islands:
                continue
            if islands[r, c] is islands[nr, nc]:
                continue
            islands[r, c].update(islands[nr, nc])
            for (lr, lc) in islands[nr, nc]:
                islands[lr, lc] = islands[r, c]
    dedup = {}

    for k, v in islands.items():
        if v not in dedup.values():
            dedup[k] = v
    sizes = [len(v) for v in dedup.values()]
    sizes.sort()
    return math.prod(sizes[-3:])


data = get_data(day=9, year=2021)
print(part1(data))
print(part2(data))
