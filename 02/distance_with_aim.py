directions = []
with open('input.txt', 'r') as in_file:
    directions = in_file.read().splitlines()


depth = 0
distance = 0
aim = 0

for direction in directions:
    command = direction.split()[0]
    amount = int(direction.split()[1])
    match command:
        case 'forward':
            distance += amount
            depth += aim * amount
        case 'down':
            aim += amount
        case 'up':
            aim -= amount
print(depth * distance)
