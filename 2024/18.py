from tqdm import tqdm

input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
input = open("18.txt", "r").read()
input = input.split()
falling_bytes: list[tuple[int, int]] = [
    (int(x), int(y)) for x, y in [item.split(",") for item in input]
]
start = (0, 0)
end = (70, 70)

vertexes: set[tuple[int, int]] = set()
dist = {}
prev = {}
for x in range(end[0] + 1):
    for y in range(end[1] + 1):
        if (x, y) not in falling_bytes[:1024]:
            vertexes.add((x, y))
            dist[(x, y)] = 1000000
dist[start] = 0
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while vertexes:
    u = (0, 0)
    for item in sorted(dist.items(), key=lambda i: i[1]):
        if item[0] in vertexes:
            u = item[0]
            break
    vertexes.remove((u[0], u[1]))
    for dir in dirs:
        v = (u[0] + dir[0], u[1] + dir[1])
        if v not in vertexes:
            continue
        alt = dist[u] + 1
        if alt < dist[v]:
            dist[v] = alt
            prev[v] = u
print("Part 1:", dist[end])
min_bytes = 0
max_bytes = len(falling_bytes)
# for bytes_to_do in tqdm(range(1023, len(falling_bytes))):
prev_bytes = 0
go_up = True
while True:
    if go_up:
        bytes_to_do = (prev_bytes + max_bytes) // 2
    else:
        bytes_to_do = (min_bytes + prev_bytes) // 2
    vertexes: set[tuple[int, int]] = set()
    dist = {}
    prev = {}
    for x in range(end[0] + 1):
        for y in range(end[1] + 1):
            if (x, y) not in falling_bytes[:bytes_to_do]:
                vertexes.add((x, y))
                dist[(x, y)] = 1000000
    dist[start] = 0
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while vertexes:
        u = (0, 0)
        for item in sorted(dist.items(), key=lambda i: i[1]):
            if item[0] in vertexes:
                u = item[0]
                break
        vertexes.remove((u[0], u[1]))
        for dir in dirs:
            v = (u[0] + dir[0], u[1] + dir[1])
            if v not in vertexes:
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    print("Trying:", bytes_to_do, end="\r")
    if bytes_to_do == 1024:
        print("Part 1:", dist[end])
    if dist[end] == 1000000:
        max_bytes = bytes_to_do
        prev_bytes = bytes_to_do
        go_up = False
    else:
        min_bytes = bytes_to_do
        prev_bytes = bytes_to_do
        go_up = True

    if abs(prev_bytes - max_bytes) == 1:
        print(
            "Part 2:",
            str(falling_bytes[prev_bytes][0]) + "," + str(falling_bytes[prev_bytes][1]),
        )
        break
