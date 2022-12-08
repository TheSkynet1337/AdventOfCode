from aocd import get_data
import numpy as np


def part1(data):
    lines = data.splitlines()
    # lines = ['30373',
    #          '25512',
    #          '65332',
    #          '33549',
    #          '35390']
    grid = np.zeros(shape=(len(lines[0]), len(lines)))
    counted = np.zeros(shape=(len(lines[0]), len(lines)))
    counted[:, 0] = 1
    counted[:, -1] = 1
    counted[0, :] = 1
    counted[-1, :] = 1
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[i, j] = int(char)
    for i in range(grid.shape[0]):
        tallest = -1
        for j in range(grid.shape[1]):
            if grid[i, j] > tallest:
                tallest = grid[i, j]
                counted[i, j] = 1
    for j in range(grid.shape[1]):
        tallest = -1
        for i in range(grid.shape[0]):
            if grid[i, j] > tallest:
                tallest = grid[i, j]
                counted[i, j] = 1
    for i in range(grid.shape[0]-1, 0, -1):
        tallest = -1
        for j in range(grid.shape[1]-1, 0, -1):
            if grid[i, j] > tallest:
                tallest = grid[i, j]
                counted[i, j] = 1
    for j in range(grid.shape[1]-1, 0, -1):
        tallest = -1
        for i in range(grid.shape[0]-1, 0, -1):
            if grid[i, j] > tallest:
                tallest = grid[i, j]
                counted[i, j] = 1
    print(np.sum(counted))
    return data


def part2(data):
    lines = data.splitlines()
    # lines = ['30373',
    #          '25512',
    #          '65332',
    #          '33549',
    #          '35390']
    grid = np.zeros(shape=(len(lines[0]), len(lines)))
    view = np.zeros(shape=(len(lines[0]), len(lines)))
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[i, j] = int(char)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            height = grid[i, j]
            left = 0
            right = 0
            up = 0
            down = 0
            for k in range(i+1, grid.shape[0]):
                if grid[k, j] < height:
                    right += 1
                else:
                    right += 1
                    break
            for k in range(i-1, -1, -1):
                if grid[k, j] < height:
                    left += 1
                else:
                    left += 1
                    break
            for k in range(j+1, grid.shape[1]):
                if grid[i, k] < height:
                    down += 1
                else:
                    down += 1
                    break
            for k in range(j-1, -1, -1):
                if grid[i, k] < height:
                    up += 1
                else:
                    up += 1
                    break
            view[i, j] = left * right * up * down
    print(np.max(view))
    return data


data = get_data(day=8, year=2022)
part1(data)

part2(data)
