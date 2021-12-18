from aocd import get_data
import time

from anytree import Node, RenderTree, PreOrderIter
import math
import json
from itertools import combinations


def build_tree(number):
    current = Node(number, value=number)
    left, right = number
    children = []
    if isinstance(left, list):
        children.append(build_tree(left))
    else:
        children.append(Node(left, value=left))
    if isinstance(right, list):
        children.append(build_tree(right))
    else:
        children.append(Node(right, value=right))
    current.children = children
    return current


def calculate_magnitude(node):
    left, right = node.children
    magnitude = 0
    if left.children:
        magnitude += 3 * calculate_magnitude(left)
    else:
        magnitude += 3 * left.value
    if right.children:
        magnitude += 2 * calculate_magnitude(right)
    else:
        magnitude += 2*right.value

    return magnitude


def explode(node):
    left = node.children[0]
    right = node.children[1]
    tree_list = list(PreOrderIter(node.root))
    left_index = tree_list.index(left)
    right_index = tree_list.index(right)
    for left_node in reversed(tree_list[:left_index]):
        if isinstance(left_node.value, int):
            left_node.value += left.value
            break
    for right_node in tree_list[right_index+1:]:
        if isinstance(right_node.value, int):
            right_node.value += right.value
            break
    node.value = 0
    node.children = []


def split_node(node):
    value = node.value
    new_left_value = math.floor(value/2)
    new_right_value = math.ceil(value/2)
    new_left = Node(str(node)+'/'+str(new_left_value),
                    value=new_left_value)
    new_right = Node(str(node)+'/'+str(new_right_value),
                     value=new_right_value)
    node.value = [new_left_value, new_right_value]
    node.children = [new_left, new_right]


def explode_tree(root):
    todo = (list(PreOrderIter(root)))
    for node in todo:
        if node.children and node.children[0].depth > 4:
            explode(node)


def reduce_number(node):
    explode_tree(node)
    todo = list(reversed(node.root.leaves))
    while todo:
        leaf = todo.pop()
        if isinstance(leaf.value, int) and leaf.value >= 10:
            split_node(leaf)
            explode_tree(leaf.root)
            todo = list(reversed(leaf.root.leaves))


def add_snail_number_to_tree(tree, n2):
    tree2 = build_tree(n2)
    new_root = Node(hash(tree), value=[tree.value, n2])
    new_root.children = [tree, tree2]

    reduce_number(new_root)
    return new_root


def add_snail_number(n1, n2):
    tree1 = build_tree(n1)
    tree2 = build_tree(n2)
    new_root = Node(hash(tree1), value=[n1, n2])
    new_root.children = [tree1, tree2]
    reduce_number(new_root)
    return new_root


def part1(data):
    data = data.splitlines()
    lists = []
    for line in data:
        lists.append(json.loads(line))

    start = build_tree(lists[0])
    curr_sum = start
    for number in lists[1:]:
        curr_sum = add_snail_number_to_tree(curr_sum, number)

    return calculate_magnitude(curr_sum)


def part2(data):
    data = data.splitlines()
    lists = []
    for line in data:
        lists.append(json.loads(line))
    combos = combinations(lists, 2)
    highest = 0
    for combo in combos:
        num = add_snail_number(combo[0], combo[1])
        num2 = add_snail_number(combo[1], combo[0])
        score = calculate_magnitude(num)
        score2 = calculate_magnitude(num2)
        if score > highest:
            highest = score
        if score2 > highest:
            highest = score2
    return highest


data = get_data(day=18, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
