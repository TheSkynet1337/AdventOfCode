input = """AAAA
BBCD
BBCC
EEEC
"""
input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
# input = open("12.txt", "r").read()
input = input.split()


def grow_area(input, cur_coord, letter, seen):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dir in dirs:
        next_coord = (cur_coord[0] + dir[0], cur_coord[1] + dir[1])
        if (
            next_coord[0] < 0
            or next_coord[0] >= len(input)
            or next_coord[1] < 0
            or next_coord[1] >= len(input[0])
        ):
            continue
        next = input[next_coord[0]][next_coord[1]]
        if next == letter and next_coord not in seen:
            seen.add(next_coord)
            seen.update(grow_area(input, next_coord, letter, seen))
    return seen


already_checked = []
areas = []
for x, row in enumerate(input):
    for y, col in enumerate(row):
        cur = (x, y)
        start_set = set()
        start_set.add(cur)
        if cur in already_checked:
            continue
        found = grow_area(input, (x, y), input[x][y], start_set)
        areas.append(found)
        for coord in found:
            already_checked.append(coord)
overall_price = 0
for area in areas:
    size = len(area)
    total_fences = 0
    for field in area:
        fences = 4
        for other in area:
            if field == other:
                pass
            # check if neighboor
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dir in dirs:
                if field[0] + dir[0] == other[0] and field[1] + dir[1] == other[1]:
                    fences -= 1
        total_fences += fences
    overall_price += size * total_fences
print("Part 1:", overall_price)
