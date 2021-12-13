from aocd import get_data
import numpy as np


def fold_paper(coords, fold):
    direction, location = fold
    newcoords = []
    location = int(location)
    for x, y in coords:
        if direction == 'x' and x > location:
            dx = x-location
            newcoords.append((location-dx, y))
        elif direction == 'y' and y > location:
            dy = y-location
            newcoords.append((x, location-dy))
        else:
            newcoords.append((x, y))
    return set(newcoords)


def part1(data):
    data = data.splitlines()

    coords = [list(map(int, coord.split(',')))
              for coord in data[:data.index('')]]
    folds = data[data.index('')+1:]
    folds = [fold.replace('fold along ', '').split('=') for fold in folds]

    return len(fold_paper(coords, folds[0]))


def part2(data):
    data = data.splitlines()
    coords = [list(map(int, coord.split(',')))
              for coord in data[:data.index('')]]
    folds = data[data.index('')+1:]
    folds = [fold.replace('fold along ', '').split('=') for fold in folds]

    for fold in folds:
        coords = fold_paper(coords, fold)

    xmax, ymax = [max(x) for x in zip(*coords)]

    letters = ''
    for w in range(ymax+1):
        for h in range(xmax+1):
            if (h, w) in coords:
                letters += '#'
            else:
                letters += ' '
        letters += '\n'
    return letters


data = get_data(day=13, year=2021)
print(part1(data))
print(part2(data))
