import time
from functools import cache

input = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''
input = open('19.txt', 'r').read()
input = input.split('\n\n')
towels = tuple([towel.strip() for towel in input[0].split(',')])
patterns = [towel.strip() for towel in input[1].split()]


@cache
def is_pattern_possible(pattern: str, towels: tuple[str]):
    if pattern == '':
        return 1
    return sum([is_pattern_possible(pattern[len(item):], towels)
                for item in filter(lambda t: pattern.find(t) == 0, towels)])


start = time.perf_counter_ns()
print('Part 1:', sum([is_pattern_possible(pattern, towels) > 0
      for pattern in patterns]))
end = time.perf_counter_ns()
print(f'Part 1 Time: {(end-start)/1e+6}ms')
start = time.perf_counter_ns()
print('Part 2:', sum([is_pattern_possible(pattern, towels)
      for pattern in patterns]))
end = time.perf_counter_ns()
print(f'Part 2 Time: {(end-start)/1e+6}ms')
