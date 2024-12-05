from tabnanny import check

input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
input = open("05.txt", "r").read()
input = input.split("\n\n")
rules = input[0].split("\n")
lines = [line.split(",") for line in input[1].split("\n")]
rules_dict = {}
for rule in rules:
    first, second = rule.split("|")
    if rules_dict.get(first) != None:
        rules_dict[first].append(second)
    else:
        rules_dict[first] = [second]
good_lines = []
bad_lines = []


def check_line(line, rules):
    rev = list(reversed(line))
    for i, num in enumerate(rev):
        if rules_dict.get(num):
            for rule in rules_dict[num]:
                if rule in rev[i:]:
                    return (False, rule, num)
    return (True, "", "")


for line in lines:
    if check_line(line, rules)[0]:
        good_lines.append(line)
    else:
        bad_lines.append(line)

good_lines = (
    good_lines[: len(good_lines) - 1]
    if good_lines[len(good_lines) - 1] == [""]
    else good_lines
)


def fix_line(line: list[str], rule, num):
    ruleidx = line.index(rule)
    numidx = line.index(num)
    line[ruleidx] = num
    line[numidx] = rule
    check = check_line(line, rules)
    if check[0]:
        fixxed_lines.append(line)
        # return line
    else:
        fix_line(line, check[1], check[2])


fixxed_lines = []
for line in bad_lines:
    check = check_line(line, rules)
    # fixxed_lines.append(fix_line(line, check[1], check[2]))
    fix_line(line, check[1], check[2])

print("Part 1:", sum([int(line[int(len(line) / 2)]) for line in good_lines]))
print("Part 2:", sum([int(line[int(len(line) / 2)]) for line in fixxed_lines]))
