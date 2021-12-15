from aocd import get_data
import numpy as np
import statistics
from collections import Counter
import time
import heapq as hq
import math
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import dok_matrix
from scipy.sparse import csr_matrix


def create_graph_from_M(M):
    m, n = M.shape
    mn = m*n
    graph = dok_matrix((mn, mn))
    for x in range(m):
        for y in range(m):
            if 0 <= x*m+y+1 < mn and 0 <= x*m+y < mn and 0 <= y+1 < M.shape[1]:
                graph[(x*m+y, x*m+y+1)] = M[x][y+1]
            if 0 <= x*m+y-1 < mn and 0 <= x*m+y < mn and 0 <= y-1 < M.shape[1]:
                graph[(x*m+y, x*m+y-1)] = M[x][y-1]
            if 0 <= x*m+y-m < mn and 0 <= x*m+y < mn and 0 <= x-1 < M.shape[0]:
                graph[(x*m+y, x*m+y-m)] = M[x-1][y]
            if 0 <= x*m+y+m < mn and 0 <= x*m+y < mn and 0 <= x+1 < M.shape[0]:
                graph[(x*m+y, x*m+y+m)] = M[x+1][y]

    return graph


def part1(data):
    data = data.splitlines()

    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    M = np.array(int_rows)
    dangers = {}
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    m, n = M.shape

    for x, y in np.ndindex(M.shape):
        dangers[(x, y)] = dangers.get((x, y), {})
        for dx, dy in directions:
            if 0 <= x+dx < M.shape[0] and 0 <= y+dy < M.shape[1]:
                danger = M[x+dx][y+dy]
                dangers[(x, y)].update({(x+dx, y+dy): danger})
    mn = m*n
    graph = create_graph_from_M(M)
    dists = shortest_path(csgraph=graph, indices=0)

    return dists[-1]


def part2(data):
    data = data.splitlines()

    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    M = np.array(int_rows)
    orig = M
    new_M = np.empty(1)
    for x in range(5):
        slice = M+x
        for y in range(5):
            if not y:
                continue
            slice = np.append(slice, orig+x+y, axis=0)
            np.subtract(slice, 9, slice, where=slice > 9)
        if not x:
            new_M = slice
        else:
            new_M = np.append(new_M, slice, axis=1)

    M = new_M

    graph = create_graph_from_M(M)
    dists = shortest_path(csgraph=graph, indices=0)

    return dists[-1]


data = get_data(day=15, year=2021)
start = time.perf_counter_ns()
print(part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print(part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
