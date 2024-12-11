from functools import cache

from tqdm import tqdm

input = """125 17"""
input = open("11.txt", "r").read()
input = [int(item) for item in input.split()]
iters = 25
stones = input
for i in tqdm(range(iters)):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[int(len(str(stone)) / 2) :]))
            new_stones.append(int(str(stone)[: int(len(str(stone)) / 2)]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
print("Part 1:", len(stones))


@cache
def do_stone(num, iters):
    stone = num
    if iters == 0:
        return 1
    if stone == 0:
        return do_stone(1, iters - 1)
    if len(str(stone)) % 2 == 0:
        return do_stone(
            int(str(stone)[int(len(str(stone)) / 2) :]), iters - 1
        ) + do_stone(int(str(stone)[: int(len(str(stone)) / 2)]), iters - 1)
    else:
        return do_stone(stone * 2024, iters - 1)


nums = []
for stone in input:
    nums.append(do_stone(stone, 75))

print("Part 2:", sum(nums))
