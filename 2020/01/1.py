from aocd import get_data


def part1(data):
    lines = list(map(int, data.splitlines()))
    lines.sort()
    for a, b in zip(lines, lines[1:]):
        if a+b == 2020:
            return a*b

    return


def part2(data):

    lines = list(map(int, data.splitlines()))
    lines.sort()
    # print(lines)
    for a in lines:
        for b in lines:
            for c in lines:
                if a+b+c == 2020:
                    return a*b*c

    return


data = get_data(day=1, year=2020)
print(part1(data))
print(part2(data))
