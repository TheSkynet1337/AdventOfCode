from aocd import get_data
import numpy as np
import math


def build_graph(edges):
    graph = {}
    for edge in edges:
        start, end = edge.split('-')
        if start in graph:
            if start != 'start' and end != 'end':
                if end in graph:
                    graph[end].append(start)
                else:
                    graph[end] = [start]
            graph[start].append(end)

        else:
            if start != 'start' and end != 'end':
                if end in graph:
                    graph[end].append(start)
                else:
                    graph[end] = [start]
            graph[start] = [end]
    return graph


def part1(data):
    data = data.splitlines()
    graph = build_graph(data)
    paths = []
    todo = []
    for start in graph['start']:
        todo.append(['start', start])
    while todo:
        it = todo.pop()
        last = it[-1]
        if last == 'end':
            paths.append(it)
            continue
        for node in graph[last]:
            if node.isupper() or node not in it:
                tmp = it + [node]
                todo.append(tmp)

    return len(paths)


def part2(data):
    data = data.splitlines()
    graph = build_graph(data)
    paths = []
    small_caves = []
    for node in graph:
        if node not in ('start', 'end') and node.islower():
            small_caves.append(node)

    for cave in small_caves:
        print(f'Doing cave {cave}')
        todo = []
        for start in graph['start']:
            todo.append(['start', start])
        while todo:
            it = todo.pop()
            last = it[-1]
            if last == 'end':
                if it not in paths:
                    paths.append(it)
                continue
            for node in graph[last]:
                if node.isupper() or node not in it or (node == cave and it.count(node) < 2):
                    tmp = it + [node]
                    todo.append(tmp)
    return len(paths)


data = get_data(day=12, year=2021)
print(part1(data))
print(part2(data))
