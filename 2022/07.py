from aocd import get_data
import numpy as np


class Dir:
    subdirs = []
    files = []
    parent = None

    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.files = []

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)
        subdir.parent = self

    def add_file(self, file, size):
        self.files.append((file, size))

    def get_size(self):
        size = 0
        for file in self.files:
            size += int(file[1])
        for subdir in self.subdirs:
            size += subdir.get_size()
        return size


def build_small_dirs(root):
    small_dirs = []
    for subdir in root.subdirs:
        if subdir.get_size() < 100000:
            small_dirs.append(subdir.get_size())
        if len(subdir.subdirs) > 0:
            small_dirs.append(build_small_dirs(subdir))
    return small_dirs


def build_dir_sizes(root):
    dir_sizes = []
    for subdir in root.subdirs:
        dir_sizes.append(subdir.get_size())
        if len(subdir.subdirs) > 0:
            dir_sizes.append(build_dir_sizes(subdir))
    return dir_sizes


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


def build_dir_tree(data):
    lines = data.splitlines()
    root = Dir("root")
    current_dir = root
    for line in lines:
        if line == "$ cd /":
            continue
        elif line == "$ cd ..":
            current_dir = current_dir.parent
            continue
        elif line.startswith("$ cd "):
            target_dir_name = line.replace("$ cd ", "")
            target_dir = next(
                dirr for dirr in current_dir.subdirs if dirr.name == target_dir_name)
            current_dir = target_dir
        elif line.startswith("dir"):
            dir_name = line.replace("dir ", "")
            dirr = Dir(dir_name)
            current_dir.add_subdir(dirr)
        elif line.startswith("$ ls"):
            continue
        else:
            size, file_name = line.split()
            current_dir.add_file(file_name, size)
    return root


def part1(data):
    root = build_dir_tree(data)
    small_dirs = []
    small_dirs.append(build_small_dirs(root))
    flat_dirs = flatten(small_dirs)
    if(root.get_size() < 100000):
        flat_dirs.append(root.get_size())
    print(sum(flat_dirs))
    return data


def part2(data):
    root = build_dir_tree(data)
    free_space = 70000000 - root.get_size()
    needed_space = 30000000
    space_to_free = needed_space - free_space
    dir_sizes = []
    dir_sizes.append(build_dir_sizes(root))
    flat_dirs = flatten(dir_sizes)
    flat_dirs.append(root.get_size())
    dirs = [dirr for dirr in flat_dirs if dirr >= space_to_free]
    dirs.sort()
    print(dirs[0])
    return data


data = get_data(day=7, year=2022)
part1(data)

part2(data)
