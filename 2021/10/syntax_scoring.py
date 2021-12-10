from aocd import get_data
import statistics
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def find_pairs(line) -> int:
    if line == None:
        return 0

    open_arrow = 0
    open_square = 0
    open_round = 0
    open_curly = 0
    for i, c in enumerate(line):
        if c == '<':
            open_arrow += 1
        elif c == '>':
            open_arrow -= 1
            if open_arrow < 0:
                print(f'found unexpected {c}')
                return scores[c]
            if line[i-1] == '<':
                return find_pairs(line[0:i-1]+line[i+1:])

            else:
                print(f'found unexpected {c}')
                return scores[c]
        elif c == '[':
            open_square += 1
        elif c == ']':
            open_square -= 1
            if open_arrow < 0:
                print(f'found unexpected {c}')
                return scores[c]
            if line[i-1] == '[':
                return find_pairs(line[0:i-1]+line[i+1:])

            else:
                print(f'found unexpected {c}')
                return scores[c]
        elif c == '(':
            open_round += 1
        elif c == ')':
            open_round -= 1
            if open_arrow < 0:
                print(f'found unexpected {c}')
                return scores[c]
            if line[i-1] == '(':
                return find_pairs(line[0:i-1]+line[i+1:])

            else:
                print(f'found unexpected {c}')
                return scores[c]
        elif c == '{':
            open_curly += 1
        elif c == '}':
            open_curly -= 1
            if open_curly < 0:
                print(f'found unexpected {c}')
                return scores[c]
            if line[i-1] == '{':
                return find_pairs(line[0:i-1]+line[i+1:])
            else:
                print(f'found unexpected {c}')
                return scores[c]
    return 0


def part1(data):
    lines = data.splitlines()

    # lines = [
    #     '[({(<(())[]>[[{[]{<()<>>',
    #     '[(()[<>])]({[<{<<[]>>(',
    #     '{([(<{}[<>[]}>{[]{[(<()>',
    #     '(((({<>}<{<{<>}{[]{[]{}',
    #     '[[<[([]))<([[{}[[()]]]',
    #     '[{[{({}]{}}([{[{{{}}([]',
    #     '{<[[]]>}<{[{[{[]{()[[[]',
    #     '[<(<(<(<{}))><([]([]()',
    #     '<{([([[(<>()){}]>(<<{{',
    #     '<{([{{}}[<[[[<>{}]]]>[]]'
    # ]
    error_score = 0
    for line in lines:
        score = find_pairs(line)
        error_score += score

    return error_score


complete_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part2(data):

    lines = data.splitlines()
    # lines = [
    #     '[({(<(())[]>[[{[]{<()<>>',
    #     '[(()[<>])]({[<{<<[]>>(',
    #     '{([(<{}[<>[]}>{[]{[(<()>',
    #     '(((({<>}<{<{<>}{[]{[]{}',
    #     '[[<[([]))<([[{}[[()]]]',
    #     '[{[{({}]{}}([{[{{{}}([]',
    #     '{<[[]]>}<{[{[{[]{()[[[]',
    #     '[<(<(<(<{}))><([]([]()',
    #     '<{([([[(<>()){}]>(<<{{',
    #     '<{([{{}}[<[[[<>{}]]]>[]]'
    # ]
    correct = list(filter(lambda l: not find_pairs(l), lines))

    score = []
    for line in correct:
        reverse = line[::-1]
        complete = []
        open_arrow = 0
        open_square = 0
        open_round = 0
        open_curly = 0
        for c in reverse:
            if c == '<':
                open_arrow += 1
                if open_arrow > 0:
                    complete.append('>')
                    open_arrow -= 1
            if c == '[':
                open_square += 1
                if open_square > 0:
                    complete.append(']')
                    open_square -= 1
            if c == '(':
                open_round += 1
                if open_round > 0:
                    complete.append(')')
                    open_round -= 1

            if c == '{':
                open_curly += 1
                if open_curly > 0:
                    complete.append('}')
                    open_curly -= 1

            if c == '>':
                open_arrow -= 1
            if c == ']':
                open_square -= 1
            if c == ')':
                open_round -= 1
            if c == '}':
                open_curly -= 1
        print(line)
        print(complete)
        s = 0
        for c in complete:
            s *= 5
            s += complete_scores[c]
        score.append(s)
    score.sort()
    print(len(score))
    return statistics.median(score)


data = get_data(day=10, year=2021)
print(part1(data))
print(part2(data))
