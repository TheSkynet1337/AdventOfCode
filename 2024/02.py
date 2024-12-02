input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
input = open('02.txt', 'r').read()
lines = input.splitlines()
safe = 0
pt1safe = 0


def try_line(nums):
    safeline = True
    increasing = nums[0] - nums[1] > 0
    for x, y in zip(nums, nums[1:]):
        if abs(x-y) > 3 or x == y or ((x-y > 0) != increasing):
            safeline = False
            break
    return safeline


for line in lines:
    nums = list(map(int, line.split()))
    if try_line(nums):
        safe += 1
        pt1safe += 1
    else:
        for i in range(len(nums)):
            if try_line(nums[:i]+nums[i+1:]):
                safe += 1
                break
print('Part 1:', pt1safe)
print('Part 2:', safe)
