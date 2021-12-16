from aocd import get_data
import numpy as np
import time


class AST:
    def __init__(self, root_pkg):
        self.root = root_pkg

    def print_AST(self, tree):
        if tree:
            print(tree)
            if tree.children:
                for node in tree.children:
                    self.print_AST(node)
        return


class Package:
    def __init__(self, version, type, value, children=None):
        self.version = version
        self.type = type
        self.value = value
        self.children = children

    def __str__(self):
        return f'Package with Version {self.version} of Type {self.type} and Value {self.value}'


def hextobin(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)


def parse_package(bits):
    version = int(bits[:3], 2)
    type = int(bits[3:6], 2)
    if type == 4:
        value = ''
        parsed = 6
        for part in (bits[i:i+5] for i in range(6, len(bits), 5)):
            value += part[1:]
            parsed += 5
            if part[0] == '0':
                int_value = int(value, 2)
                #  print(f'Adding Package with {value} to AST')
                pkg = Package(version, type, int_value)
                rest = bits[parsed:]
                tmp = rest.replace('0', '')
                if tmp:
                    #    print('rest', rest)
                    #    print(pkg)
                    return rest, pkg
                else:
                   # AST.tree.append(pkg)
                    return '', pkg
    else:
        ID = int(bits[6], 2)
        # print('ID', ID)
        if ID:
            package_num = int(bits[7:18], 2)
       #     print('packageN:', package_num)
            new_bits = bits[18:]
            # print(f'Adding {bits} to AST')
            children = []
            pkg = Package(version, type, new_bits, children)
            for i in range(package_num):
                # print('i', i)
                # print(f'Parsing contained Package {i+1}')
                # print(f'Parsing: {new_bits}')
                new_bits = parse_package(new_bits)
                # print(f'new bits{new_bits}')
                if new_bits:
                 #   print(f'Adding {new_bits[1]} as children.')
                    pkg.children.append(new_bits[1])
                    new_bits = new_bits[0]
            if new_bits:
                # pkg.children = children
                return new_bits, pkg

        else:
            package_len = int(bits[7:22], 2)
            parsed = 0
            rest = ''
            rest = bits[22:]
            previous = 0
            children = []
            pkg = Package(version, type, rest, children)
            while rest:
                old = rest
                rest = parse_package(rest)

                if rest:
                    pkg.children.append(rest[1])
                    rest = rest[0]
                    parsed += len(old)-len(rest)
                    if parsed >= package_len:
                        return rest, pkg
    return '', pkg


def print_parsed_AST(root, indent):
    formula = ''
    tree = root
    for _ in range(indent):
        formula += '  '
    if tree:

        if tree.type != 4:
            formula += '('
        match tree.type:
            case 0:
                formula += '+\n'
            case 1:
                formula += '*\n'
            case 2:
                formula += 'min\n'
            case 3:
                formula += 'max\n'
            case 5:
                formula += '>\n'
            case 6:
                formula += '<\n'
            case 7:
                formula += '=\n'
            case 4:
                formula += str(tree.value) + '\n'
        if tree.children:
            for node in tree.children:
                formula += print_parsed_AST(node, indent+1)
        else:
            return formula
    re = ''
    for _ in range(indent):
        re += '  '
    return formula + re + ')\n'


def parse_AST(root):
    result = 0
    tree = root
    if tree:
        match tree.type:
            case 0:
                for node in tree.children:
                    result += parse_AST(node)
            case 1:
                tmp = []
                for node in tree.children:
                    tmp.append(parse_AST(node))
                prod = 1
                for num in tmp:
                    prod *= num
                result += prod
            case 2:
                tmp = []
                for node in tree.children:
                    tmp.append(parse_AST(node))
                result = min(tmp)
            case 3:
                tmp = []
                for node in tree.children:
                    tmp.append(parse_AST(node))
                result = max(tmp)
            case 5:
                if parse_AST(tree.children[0]) > parse_AST(
                        tree.children[1]):
                    result = 1
                else:
                    result = 0
            case 6:
                if parse_AST(tree.children[0]) < parse_AST(
                        tree.children[1]):
                    result = 1
                else:
                    result = 0

            case 7:
                if parse_AST(tree.children[0]) == parse_AST(
                        tree.children[1]):
                    result = 1
                else:
                    result = 0
            case 4:
                result = tree.value
    return result


def vsum_ast(root):
    vsum = 0
    tree = root
    if tree:
        vsum += tree.version
        if tree.children:
            for node in tree.children:
                vsum += vsum_ast(node)
    return vsum


def part1(data):
    data = data.splitlines()
    # data = [
    # 'D2FE28',
    # 'EE00D40C823060',
    # '38006F45291200',
    # '8A004A801A8002F478',
    # '620080001611562C8802118E34',
    # 'C0015000016115A2E0802F182340',
    # 'A0016C880162017C3686B18A3D4780'
    # ]
    h = data[0]
    print(f'Parsing Hex:{h}')
    bits = hextobin(h)
    ast = AST(parse_package(bits)[1])
    vsum = vsum_ast(ast.root)

    return vsum


def part2(data):
    data = data.splitlines()
    # data = [
    # 'C200B40A82'
    # '04005AC33890'
    # '880086C3E88112'
    # 'CE00C43D881120'
    # 'D8005AC2A8F0'
    # 'F600BC2D8F'
    # '9C005AC2F8F0'
    # '9C0141080250320F1802104A08'
    # ]
    h = data[0]
    print(f'Parsing Hex:{h}')
    bits = hextobin(h)
    ast = AST(parse_package(bits)[1])
    print(print_parsed_AST(ast.root, 0))
    print(parse_AST(ast.root))

    return


data = get_data(day=16, year=2021)
start = time.perf_counter_ns()
print('Part1: ', part1(data))
end = time.perf_counter_ns()
print(f'Part1 Time: {(end-start)/1e+6}ms')

start = time.perf_counter_ns()
print('Part2: ', part2(data))
end = time.perf_counter_ns()
print(f'Part2 Time: {(end-start)/1e+6}ms')
