from aocd import get_data


def part1(data):
    ind = data.splitlines()
    ind = [d.split(': ') for d in ind]
    req = [d[0].split(' ') for d in ind]
    len_req = [list(map(int, r[0].split('-'))) for r in req]
    min_len = [r[0] for r in len_req]
    max_len = [r[1] for r in len_req]
    char_req = [c[1] for c in req]
    pws = [pw[1] for pw in ind]
    return sum([min_c <= pw.count(c) <= max_c
                for min_c, max_c, c, pw in zip(min_len, max_len, char_req, pws)])


def part2(data):
    ind = data.splitlines()
    ind = [d.split(': ') for d in ind]
    req = [d[0].split(' ') for d in ind]
    len_req = [list(map(int, r[0].split('-'))) for r in req]
    min_len = [r[0] for r in len_req]
    max_len = [r[1] for r in len_req]
    char_req = [c[1] for c in req]
    pws = [pw[1] for pw in ind]
    return sum([(c == pw[min_c-1]) != (c == pw[max_c-1])
                for min_c, max_c, c, pw in zip(min_len, max_len, char_req, pws)])
    return


data = get_data(day=2, year=2020)
print(part1(data))
print(part2(data))
