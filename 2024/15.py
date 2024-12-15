import time

input = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''
xinput = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''


def paint(house: list[str], boxes: set[tuple[int, int]], walls: set[tuple[int, int]], robot: tuple[int, int]):
    for x, row in enumerate(house):
        line: list[str] = []
        for y, _ in enumerate(row):
            if (x, y) in boxes:
                line.append('O')
            elif (x, y) in walls:
                line.append('#')
            elif (x, y) == robot:
                line.append('@')
            else:
                line.append('.')
        print(''.join(line))
    print('-'*len(row))


def movable(robot: tuple[int, int], boxes: set[tuple[int, int]], walls: set[tuple[int, int]], dir: tuple[int, int]):
    res = []
    next_coord = (robot[0]+dir[0], robot[1] + dir[1])
    if next_coord in boxes:
        over_next_coord = (next_coord[0]+dir[0], next_coord[1] + dir[1])
        if over_next_coord in walls:
            return res + [False]
        elif over_next_coord in boxes:
            return res + [True] + movable(next_coord, boxes, walls, dir)

        else:
            return res + [True]


def part1():
    input = open('15.txt', 'r').read()
    input = input.split('\n\n')
    house = input[0].split()
    moves = input[1].replace('\n', '')
    # for line in house:
    #     print(line)
    # print(moves)
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    walls: set[tuple[int, int]] = set()
    boxes: set[tuple[int, int]] = set()
    robot = (0, 0)
    for x, row in enumerate(house):
        for y, char in enumerate(row):
            if char == '#':
                walls.add((x, y))
            elif char == 'O':
                boxes.add((x, y))
            elif char == '@':
                robot = (x, y)

    for move in moves:
        dir = dirs[move]
        next_coord = (robot[0]+dir[0], robot[1] + dir[1])
        if next_coord in walls:
            continue
        if next_coord in boxes:
            boxes_to_move = movable(robot, boxes, walls, dir)
            if False in boxes_to_move:
                boxes_to_move = 0
            else:
                boxes_to_move = sum(boxes_to_move)
            if boxes_to_move > 0:
                boxes.remove(next_coord)
                boxes.add((next_coord[0]+dir[0]*boxes_to_move,
                          next_coord[1]+dir[1]*boxes_to_move))
            else:
                continue
        robot = next_coord
        # paint(house, boxes, walls, robot)

    gps = 0
    for box in boxes:
        gps += box[0]*100+box[1]
    return gps


# paint(house, boxes, walls, robot)
start = time.perf_counter_ns()
gps = part1()
end = time.perf_counter_ns()
print('Part 1:', gps)
print(f'Part1 Time: {(end-start)/1e+6}ms')
