from collections import Counter

input = []
with open('01.txt', 'r') as f:
    input = list(map(int, f.read().split()))
part1_sum = sum([abs(pair[0] - pair[1])
                 for pair in zip(sorted(input[::2]), sorted(input[1::2]))])
print('Part 1:', part1_sum)
right_dict = Counter(input[1::2])
similiarity = sum([left_num * right_dict[left_num]
                   for left_num in input[::2]])
print('Part 2:', similiarity)
