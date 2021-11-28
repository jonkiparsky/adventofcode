PROBLEM_BASENAME = "day8"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)
import re
from collections import defaultdict


pat = re.compile("(\w\w\w) ([+-]\d+)")

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.readlines()
    return [process(row.strip()) for row in rows]

def process(row):
    opcode, arg = pat.match(row).groups()
    return opcode, int(arg)


def acc(argument, accumulator, address):
    return address + 1, accumulator + argument

def jmp(argument, accumulator, address):
    return address + argument, accumulator

def nop(argument, accumulator, address):
    return address + 1, accumulator

operations = {"acc": acc,
              "jmp": jmp,
              "nop": nop}

def operation(address, accumulator, instruction):
    opcode, arg = instruction
    return operations[opcode](arg, accumulator, address)

def execute(instructions, debug=False):
    seen = [] 
    if debug:
        import pdb; pdb.set_trace()
    acc = 0
    current_address = 0
    while True:
        if seen.count(current_address)==2:
            return acc, current_address, seen
        if current_address> len(instructions):
            return "SUCCESS", acc
        seen.append(current_address)        
        current_address, acc = operation(current_address, acc, instructions[current_address])
        

    return acc


def try(instructions, instruction):

sample = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")

sample_instructions = [process(row) for row in sample]




