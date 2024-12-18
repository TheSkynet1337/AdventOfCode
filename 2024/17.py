import re

from tqdm import tqdm
from z3 import BitVec, Optimize

input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
input = open("17.txt", "r").read()
input = input.split("\n\n")


def part1():
    A, B, C = [int(item) for item in re.findall(r"\d+", input[0])]
    program = [int(item.strip()) for item in input[1].split(":")[1].split(",")]
    instructions = [(inst, op) for inst, op in zip(program[::2], program[1::2])]
    i_pointer = 0
    out = []

    print(A, B, C, instructions)

    def resolve_combo_op(operand: int) -> int:
        match operand:
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case _:
                return operand

    while i_pointer < len(instructions):
        instruction, operand = instructions[i_pointer]
        # i_pointer += 1
        # match instruction:
        #     case 0:
        #         A = A // 2 ** resolve_combo_op(operand)
        #     case 1:
        #         B = B ^ operand
        #     case 2:
        #         B = resolve_combo_op(operand) % 8
        #     case 3:
        #         if A == 0:
        #             pass
        #         else:
        #             i_pointer = operand // 2
        #     case 4:
        #         B = B ^ C
        #     case 5:
        #         out.append(str(resolve_combo_op(operand) % 8))
        #     case 6:
        #         B = A // 2 ** resolve_combo_op(operand)
        #     case 7:
        #         C = A // 2 ** resolve_combo_op(operand)
        i_pointer += 1
        B = A % 8
        i_pointer += 1
        B = B ^ 3
        i_pointer += 1
        C = A // 2**B
        i_pointer += 1
        B = B ^ C
        i_pointer += 1
        B = B ^ 3
        i_pointer += 1
        A = A // 2**3
        i_pointer += 1
        out.append(str(B % 8))
        i_pointer += 1
        if A == 0:
            pass
        else:
            i_pointer = 0
    print("out:", ",".join(out))


part1()
