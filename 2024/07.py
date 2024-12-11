from tqdm import tqdm

input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
input = open("07.txt", "r").read()
input = input.split("\n")[:-1]
input = [line.split(":") for line in input]
valid_sums = set()


def print_sum(res, nums, mask):
    sum_str = str(res) + " = " + str(nums[0])
    for n, m in zip(nums, mask):
        if m == "1":
            sum_str += "*" + str(n)
        if m == "0":
            sum_str += "+" + str(n)
    return sum_str


def print_tern_sum(res, nums, mask):
    sum_str = str(res) + " = " + str(nums[0])
    for n, m in zip(nums, mask):
        if m == "1":
            sum_str += "*" + str(n)
        if m == "0":
            sum_str += "+" + str(n)
        if m == "2":
            sum_str += str(n)
    return sum_str


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))


for line in input:
    left, right = line
    left = int(left)
    right = [int(item) for item in right.split()]
    for i in range(2 ** len(right)):
        cur_sum = 0
        mask = format(i, "b").zfill(len(right))
        assert len(mask) == len(right)
        for i, pair in enumerate(zip(mask, right)):
            m, char = pair
            if i == 0:
                cur_sum += char
                continue
            if m == "1":
                cur_sum = cur_sum * char
            if m == "0":
                cur_sum = cur_sum + char
        if cur_sum == left:
            valid_sums.add((left, "".join([str(item) for item in right])))

valid_sum = 0
for left, right in valid_sums:
    valid_sum += left
print("Part 1:", valid_sum)
pt2_valid_sums = set()
masks = {}
_, right = input[0]
for line in tqdm(input):
    left, right = line
    left = int(left)
    right = [int(item) for item in right.split()]
    res = {}
    lens = []
    for i in range(3 ** len(right)):
        cur_sum = 0
        if masks.get((len(right), i)):
            tern_mask = masks[(len(right), i)]
        else:
            masks[(len(right), i)] = ternary(i).zfill(len(right))
            tern_mask = masks[(len(right), i)]
        assert len(tern_mask) == len(right)
        # if i > 3:
        #     oneidx = tern_mask.index("1")
        #     twoidx = tern_mask.index("2")
        #     if oneidx < twoidx:
        #         idx = oneidx
        #         short_right = right[:idx]
        #         short_mask = tern_mask[:idx]
        #         print(tern_mask, short_mask, tern_mask[idx:])
        #         cur_sum = res[tern_mask]
        #     else:
        #         idx = twoidx
        #         short_right = right[:idx]
        #         short_mask = tern_mask[:idx]
        #         cur_sum = res[tern_mask]
        #         print(tern_mask, short_mask, tern_mask[idx:])
        # else:
        short_mask = tern_mask
        short_right = right
        for i, pair in enumerate(zip(short_mask, short_right)):
            m, char = pair
            if m == "1":
                cur_sum = cur_sum * char
            if m == "0":
                cur_sum = cur_sum + char
            if m == "2":
                cur_sum = int(str(cur_sum) + str(char))
        res[tern_mask] = cur_sum
        lens.append(len(tern_mask))
        if cur_sum == left:
            pt2_valid_sums.add((left, "".join([str(item) for item in right])))
pt2_valid_sum = 0
for left, right in pt2_valid_sums:
    pt2_valid_sum += left
print("Part 2:", pt2_valid_sum)
