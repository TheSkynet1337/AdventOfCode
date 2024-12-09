input = "2333133121414131402"
input = open("09.txt", "r").read()[:-1]


class file_block:
    def __init__(self, id, size) -> None:
        self.id = id
        self.size = size

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return str(self.id)


class empty_space:
    def __init__(self, size) -> None:
        self.size = size

    def __repr__(self) -> str:
        return "." * self.size

    def __str__(self) -> str:
        return "."


uncompacted = []
pt2 = []
files = []
empties = []
for i, char in enumerate(input):
    if i % 2 == 0:
        for j in range(int(char)):
            uncompacted.append(file_block(int(i / 2), int(char)))
        file = file_block(int(i / 2), int(char))
        pt2.append(file)
        files.append(file)
    else:
        for k in range(int(char)):
            uncompacted.append(".")
        empty = empty_space(int(char))
        pt2.append(empty)
        empties.append(empty)
numdots = uncompacted.count(".")
for i in range(numdots):
    idx = uncompacted.index(".")
    if uncompacted[-1] == ".":
        uncompacted.pop()
        continue
    else:
        uncompacted[idx] = uncompacted[-1]
        uncompacted.pop()
check = [str(char) for char in uncompacted]
check = "".join(check)
filesum = 0
for i, char in enumerate(uncompacted):
    filesum += i * char.id
print("Part 1:", filesum)
for file in reversed(files):
    for empty in empties:
        if file.size <= empty.size:
            if pt2.index(empty) > pt2.index(file):
                break
            fileidx = pt2.index(file)
            pt2 = pt2[:fileidx] + [empty_space(file.size)] + pt2[fileidx + 1 :]
            idx = pt2.index(empty)
            pt2 = pt2[:idx] + [file] + pt2[idx:]
            empty.size = empty.size - file.size
            break
pt2long = []
for item in pt2:
    if type(item) == empty_space:
        pt2long += item.size * ["."]
    if type(item) == file_block:
        pt2long += item.size * [item]
filesum = 0
for i, char in enumerate(pt2long):
    if char == ".":
        continue
    else:
        filesum += i * char.id
print("Part 2:", filesum)
