import numpy as np
from collections import Counter
digitlens = {
    'zero': 6,
    'one': 2,
    'two': 5,
    'three': 5,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 3,
    'eight': 7,
    'nine':  6
}

notes = []
with open('input.txt', 'r') as in_file:
    notes = in_file.read().splitlines()

inputs = [note.split(' | ') for note in notes]
# print(inputs)
outputs = []
for _input in inputs:
    outputs.append(_input[1].split(' '))

print(outputs)
counts = Counter([len(item) for sub in outputs for item in sub])
print(counts[2]+counts[3]+counts[4]+counts[7])
