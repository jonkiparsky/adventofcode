import re
from collections import namedtuple

input_file = "/home/jon/code/adventofcode/2022/day5.txt"

initial_stacks = '''                [B]     [L]     [S]
        [Q] [J] [C]     [W]     [F]
    [F] [T] [B] [D]     [P]     [P]
    [S] [J] [Z] [T]     [B] [C] [H]
    [L] [H] [H] [Z] [G] [Z] [G] [R]
[R] [H] [D] [R] [F] [C] [V] [Q] [T]
[C] [J] [M] [G] [P] [H] [N] [J] [D]
[H] [B] [R] [S] [R] [T] [S] [R] [L]'''.split("\n")


example_instructions = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")

example_stack_picture = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]"]

pat = re.compile("move (\d+) from (\d+) to (\d+)")
instruction = namedtuple("instruction", ['count', 'origin', 'destination'])

def parse_instructions(data=None):
    data = data or open(input_file)
    return [instruction(*map(int, pat.match(row).groups())) for row in data]

def build_stacks(stack_picture=initial_stacks):
    raw_stacks = zip(* [list(row[1::4]) for row in stack_picture])
    return [[c for c in stack if c.strip()]
            for stack in raw_stacks]


def solve1(stack_picture=initial_stacks, instructions = None):
    stacks = build_stacks(stack_picture)
    instructions = parse_instructions(instructions)
    for count, origin, destination in instructions:
        for _ in range(count):
            stacks[destination-1].insert(0, stacks[origin-1].pop(0))

    return stacks

def solve2(stack_picture=initial_stacks, instructions = None):
    stacks = build_stacks(stack_picture)
    instructions = parse_instructions(instructions)
    for count, origin, destination in instructions:
        stacks[destination-1] = stacks[origin-1][:count] + stacks[destination-1]
        stacks[origin-1] = stacks[origin-1][count:]
    return "".join([stack[0] for stack in stacks])
