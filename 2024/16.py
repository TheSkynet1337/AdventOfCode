import sys

input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
xinput = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
# input = open("16.txt", "r").read()
input = input.split()

walls: set[tuple[int, int]] = set()
start = (0, 0)
end = (0, 0)
step_cost = 1
for x, row in enumerate(input):
    for y, char in enumerate(row):
        if char == "#":
            walls.add((x, y))
        elif char == "S":
            start = (x, y)
        elif char == "E":
            end = (x, y)
print(input)
starts = {start: (0, 0, 1)}
print(end)
print(sys.getrecursionlimit())
sys.setrecursionlimit(30000)
print(sys.getrecursionlimit())


def find_path(input, walls, start, end, cur_dir, seen):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    costs = {}
    exited_dirs = {}
    for dir in dirs:
        next_coord = (start[0] + dir[0], start[1] + dir[1])
        if next_coord in walls:
            continue
        if next_coord in seen:
            cost = starts[next_coord]
            exited_dir = (starts[next_coord][1], starts[next_coord][2])
            dir_distance = max(abs(dir[0] - exited_dir[0]), abs(dir[1] - exited_dir[1]))
            if (
                starts[next_coord][0]
                < starts[start][0] + step_cost + dir_distance * 1000
            ):
                continue
        cur_dir_distance = max(abs(cur_dir[0] - dir[0]), abs(cur_dir[1] - dir[1]))
        starts[next_coord] = (
            starts[start][0] + step_cost + cur_dir_distance * 1000,
            dir[0],
            dir[1],
        )
        seen.add(next_coord)
        seen.update(find_path(input, walls, next_coord, end, dir, seen))
    return seen


seen = set()
seen.add(start)
find_path(input, walls, start, end, (0, 1), seen)
for k, v in starts.items():
    if k[0] == end[0] and k[1] == end[1]:
        print(k, v)
