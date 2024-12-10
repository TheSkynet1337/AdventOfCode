input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# input = open("10.txt", "r").read()
input = [[int(item) for item in line] for line in input.split()]


def search_trail(coord, cur):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    for dir in dirs:
        next_coord = (coord[0] + dir[0], coord[1] + dir[1])
        if next_coord[0] < 0 or next_coord[0] >= len(input):
            continue
        if next_coord[1] < 0 or next_coord[1] >= len(input[0]):
            continue
        next = input[coord[0] + dir[0]][coord[1] + dir[1]]
        if next - cur == 1:
            if next == 9:
                seen.add(next_coord)
            seen.update(search_trail(next_coord, next))
    return seen


def rate_trail(coord, cur):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    found = 0
    for dir in dirs:
        next_coord = (coord[0] + dir[0], coord[1] + dir[1])
        if next_coord[0] < 0 or next_coord[0] >= len(input):
            continue
        if next_coord[1] < 0 or next_coord[1] >= len(input[0]):
            continue
        next = input[coord[0] + dir[0]][coord[1] + dir[1]]
        if next - cur == 1:
            if next == 9:
                found += 1
            found += rate_trail(next_coord, next)
    return found


trails = []
ratings = []
for x, row in enumerate(input):
    for y, col in enumerate(row):
        if input[x][y] == 0:
            trails.append(search_trail((x, y), 0))
            ratings.append(rate_trail((x, y), 0))
print("Part 1:", sum([len(s) for s in trails]))
print("Part 2:", sum(ratings))
