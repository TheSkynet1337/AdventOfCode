import re

print("Part 1:", sum([int(pair[0]) * int(pair[1]) for pair in [re.findall(
    "\\d{1,3}", match) for match in re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", open("03.txt", "r").read())]]))

print("Part 2:", sum([int(pair[0]) * int(pair[1]) for pair in [re.findall("\\d{1,3}", match) for match in re.findall(
    "mul\\(\\d{1,3},\\d{1,3}\\)", "".join([dos.split("don't()")[0] for dos in open("03.txt", "r").read().split("do()")]))]]))
