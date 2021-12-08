'''
 0000
1    2
1    2
 3333
4    5
4    5
 6666
'''

positions = {}

codes = {}


def segment_to_int(seg):
    return list(codes.values()).index(seg)


def find_pos(in_line):
    in_line = in_line
    in_line[:] = [''.join(sorted(word)) for word in in_line]
    done = []
    # set possible '2' and '5' using 1
    one = [word for word in in_line if len(word) == 2][0]
    codes['one'] = one
    positions['two'] = one
    positions['five'] = one
    done.append([c for c in one])
    # set '0' using 7
    seven = [word for word in in_line if len(word) == 3][0]
    codes['seven'] = seven
    positions['zero'] = seven.replace(one[0], '').replace(one[1], '')
    done.append([c for c in seven])
    # set possible '1' and '3' using 4
    four = [word for word in in_line if len(word) == 4][0]
    codes['four'] = four
    positions['one'] = four.replace(one[0], '').replace(one[1], '')
    positions['three'] = four.replace(one[0], '').replace(one[1], '')
    done.append([c for c in four])
    # set possible '4' and '6' using 8
    eight = [word for word in in_line if len(word) == 7][0]
    codes['eight'] = eight
    done = [item for sub in done for item in sub]
    for j, c in enumerate(eight):
        if c in done:
            eight = eight.replace(c, '')
    positions['four'] = eight
    positions['six'] = eight
    # most positions are still uncertain
    fives = [word for word in in_line if len(word) == 5]
    # use the fact that 3 has '2' and '5' but 5 and 2 only have either '2' or '5' each to make '1' and '3' clear
    for candidate in fives:
        if positions['two'][0] in candidate and positions['two'][1] in candidate:
            codes['three'] = candidate
            positions['three'] = positions['three'][0] if positions['three'][0] in candidate else positions['three'][1]
            # remove 3 from candidates 2 and 5 remain
            fives.remove(candidate)
    positions['one'] = positions['one'].replace(positions['three'], '')
    for candidate in fives:
        if positions['one'] in candidate:
            codes['five'] = candidate
        else:
            codes['two'] = candidate
    sixes = [word for word in in_line if len(word) == 6]
    for candidate in sixes:
        # use the fact that 0 and 9 have '2' and '5' while 6 only has '2' to make them clear
        if positions['three'] in candidate and not (positions['two'][0] in candidate and positions['two'][1] in candidate):
            codes['six'] = candidate
            positions['five'] = positions['five'][0] if positions['five'][0] in candidate else positions['five'][1]
            # remove 6 from candidates 0 and 9 remain
            sixes.remove(candidate)
    positions['two'] = positions['two'].replace(positions['five'], '')
    # use the fact that 9 has '3' to make '6' and '4' clear since 9 only has '6'
    for candidate in sixes:
        if positions['three'] in candidate:
            codes['nine'] = candidate
            positions['six'] = positions['six'][0] if positions['six'][0] in candidate else positions['six'][1]
            # remove 9 from candidates 0 remains
            sixes.remove(candidate)
    positions['four'] = positions['four'].replace(positions['six'], '')
    codes['zero'] = sixes[0]
    # print(codes)


notes = []
with open('input.txt', 'r') as in_file:
    notes = in_file.read().splitlines()

inputs = [note.split(' | ') for note in notes]
# print(inputs)
digits_list = []
for i in inputs:
    temp_in = i[0].split(' ')
    temp_out = i[1].split(' ')
    i = [temp_in, temp_out]
    find_pos(i[0])
    digits = ''
    for output in i[1]:
        digits += str(segment_to_int(''.join(sorted(output))))
    digits_list.append(int(digits))
    positions = positions.fromkeys(positions, '')

print(sum(digits_list))
