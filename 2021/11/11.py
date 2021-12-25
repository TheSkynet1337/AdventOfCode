from aocd import get_data
import numpy as np
import statistics


def part1(data):
    data = data.splitlines()
    # data = [
    #     '5483143223',
    #     '2745854711',
    #     '5264556173',
    #     '6141336146',
    #     '6357385478',
    #     '4167524645',
    #     '2176841721',
    #     '6882881134',
    #     '4846848554',
    #     '5283751526'
    # ]
    # data = [
    #     '11111',
    #     '19991',
    #     '19191',
    #     '19991',
    #     '11111'
    # ]
    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    octos = np.array(int_rows)
    flashes = 0
    directions = [(-1, -1), (-1, 0), (1, -1), (1, 0),
                  (1, 1), (0, 1), (-1, 1), (0, -1)]
    for i in range(100):
        visited = np.zeros(octos.shape, dtype=bool)
        octos += 1
        todo = [(x, y) for x, y in zip(*np.where(octos > 9))]
        while todo:
            x, y = todo.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                if 0 <= x+dx < octos.shape[0] and 0 <= y+dy < octos.shape[1]:
                    octos[x+dx][y+dy] += 1
                    if octos[x+dx][y+dy] > 9:
                        todo.append((x+dx, y+dy))
        flashes += octos[octos > 9].size

        octos[octos > 9] = 0

    return flashes


def part2(data):

    data = data.splitlines()
    rows = [r for r in data]
    int_rows = []
    for row in rows:
        int_rows.append([int(d) for d in row])
    octos = np.array(int_rows)
    flashes = 0
    directions = [(-1, -1), (-1, 0), (1, -1), (1, 0),
                  (1, 1), (0, 1), (-1, 1), (0, -1)]
    for i in range(100000):
        visited = np.zeros(octos.shape, dtype=bool)
        octos += 1
        todo = [(x, y) for x, y in zip(*np.where(octos > 9))]
        while todo:
            x, y = todo.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                if 0 <= x+dx < octos.shape[0] and 0 <= y+dy < octos.shape[1]:
                    octos[x+dx][y+dy] += 1
                    if octos[x+dx][y+dy] > 9:
                        todo.append((x+dx, y+dy))
        if (octos > 9).all():
            print(f'synched: {i+1}')
            print(octos)
            break
        octos[octos > 9] = 0
    return


data = get_data(day=11, year=2021)
print(part1(data))
print(part2(data))
