from tqdm import tqdm

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
input = open("06.txt", "r").read()
input = input.split()
max_rows = len(input)
max_columns = len(input[0])


def find_letter(ar_of_str, letter):
    coords = []
    for row, line in enumerate(ar_of_str):
        for column, char in enumerate(line):
            if char == letter:
                coords.append((row, column))
    return coords


garbage = find_letter(input, "#")
guard_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard = find_letter(input, "^")[0]
guard_dir = (-1, 0)


def guard_in_field(guard):
    return (0 <= guard[0] < max_rows) and (0 <= guard[1] < max_columns)


patroled_fields = set()
patroled_fields.add(guard)
while guard_in_field(guard):
    step = (guard[0] + guard_dir[0], guard[1] + guard_dir[1])
    if step in garbage:
        guard_dir = guard_dirs[
            (
                guard_dirs.index(guard_dir) + 1
                if guard_dirs.index(guard_dir) + 1 < len(guard_dirs)
                else guard_dirs.index(guard_dir) + 1 - len(guard_dirs)
            )
        ]
    else:
        if not guard_in_field(step):
            break
        guard = step
        patroled_fields.add(guard)


print("Part 1:", len(patroled_fields))


guard = find_letter(input, "^")[0]
guard_dir = (-1, 0)


def try_walk(guard, guard_dir, blocker):
    patroled_fields = set()
    patroled_fields.add(guard + guard_dir)
    while guard_in_field(guard):
        step = (guard[0] + guard_dir[0], guard[1] + guard_dir[1])
        if (step in garbage) or (step[0] == blocker[0] and step[1] == blocker[1]):
            guard_dir = guard_dirs[
                (
                    guard_dirs.index(guard_dir) + 1
                    if guard_dirs.index(guard_dir) + 1 < len(guard_dirs)
                    else guard_dirs.index(guard_dir) + 1 - len(guard_dirs)
                )
            ]
        else:
            if not guard_in_field(step):
                break
            guard = step
            if guard + guard_dir in patroled_fields:
                return True
            patroled_fields.add(guard + guard_dir)
    return False


valid_blocker = []
patroled_fields.remove(guard)
for blocker in tqdm(patroled_fields):
    if try_walk(guard, (-1, 0), blocker):
        valid_blocker.append(blocker)
if guard in valid_blocker:
    valid_blocker.remove(guard)
for blocker in valid_blocker:
    if blocker in garbage:
        valid_blocker.remove(blocker)

print("Part 2:", len(valid_blocker))
