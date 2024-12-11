input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
input = open("08.txt", "r").read()
input = input.split()
letters = set()
for x, row in enumerate(input):
    for y, col in enumerate(row):
        if input[x][y] != ".":
            letters.add((input[x][y], x, y))


def part1(input, letters):
    antipodes = set()
    for letter in letters:
        for o_letter in letters:
            if letter == o_letter:
                continue
            if letter[0] != o_letter[0]:
                continue
            xd = letter[1] - o_letter[1]
            yd = letter[2] - o_letter[2]
            coords = [(letter[1], letter[2]), (o_letter[1], o_letter[2])]
            antis = []
            for coord in coords:
                x1 = coord[0] + xd
                y1 = coord[1] + yd
                if (x1, y1) not in coords:
                    antis.append((x1, y1))
            for anti in antis:
                antipodes.add(anti)
    final_antipodes = set()
    for anti in antipodes:
        if 0 <= anti[0] < len(input) and 0 <= anti[1] < len(input[0]):
            final_antipodes.add(anti)
    print("Part 1:", len(final_antipodes))
    out = input
    for anti in final_antipodes:
        line = out[anti[0]]
        line = line[: anti[1]] + "#" + line[anti[1] + 1 :]
        out[anti[0]] = line
    for line in out:
        print(line)


def part2(input, letters):
    antipodes = set()
    for letter in letters:
        for o_letter in letters:
            if letter == o_letter:
                continue
            if letter[0] != o_letter[0]:
                continue
            xd = letter[1] - o_letter[1]
            yd = letter[2] - o_letter[2]
            coords = [(letter[1], letter[2]), (o_letter[1], o_letter[2])]
            antis = []
            for coord in coords:
                x1 = coord[0] + xd
                y1 = coord[1] + yd
                next_coord = (x1, y1)
                antis.append(next_coord)
                while True:
                    next_coord = (next_coord[0] + xd, next_coord[1] + yd)
                    if (
                        next_coord[0] < 0
                        or next_coord[0] > len(input)
                        or next_coord[1] < 0
                        or next_coord[1] > len(input[0])
                    ):
                        break
                    antis.append(next_coord)
            for anti in antis:
                antipodes.add(anti)
    final_antipodes = set()
    for anti in antipodes:
        if 0 <= anti[0] < len(input) and 0 <= anti[1] < len(input[0]):
            final_antipodes.add(anti)
    print("Part 2:", len(final_antipodes))
    out = input
    for anti in final_antipodes:
        line = out[anti[0]]
        line = line[: anti[1]] + "#" + line[anti[1] + 1 :]
        out[anti[0]] = line
    for line in out:
        print(line)


part1(input, letters)
part2(input, letters)
