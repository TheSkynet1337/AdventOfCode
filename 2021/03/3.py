input = []
with open('input.txt', 'r') as in_file:
    input = in_file.read().splitlines()



gamma = ""
epsilon = ""
for i in range(len(input[0])):
    ones = 0
    for number in input:
        ones += int(number[i])
    zeros = len(input) - ones
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma,2)* int(epsilon,2))


oxygen = input
for i in range(len(input[0])):
    if len(oxygen) == 1:
        break
    temp = []
    ones = 0
    zeros = 0
    for number in oxygen:
        ones += int(number[i])
    zeros = len(oxygen) - ones
    if zeros > ones:
        for number in oxygen:
            if number[i] == '0':
                temp.append(number)
    else:
        for number in oxygen:
            if number[i] == '1':
                temp.append(number)
    oxygen = temp

print('oxygen',int(oxygen[0],2))

co2 = input
for i in range(len(input[0])):
    if len(co2) == 1:
        break
    temp = []
    ones = 0
    zeros = 0
    for number in co2:
        ones += int(number[i])
    zeros = len(co2) - ones
    if zeros <= ones:
        for number in co2:
            if number[i] == '0':
                temp.append(number)
    else:
        for number in co2:
            if number[i] == '1':
                temp.append(number)
    co2 = temp
print('co2',int(co2[0],2))
print(int(oxygen[0],2)*int(co2[0],2))
