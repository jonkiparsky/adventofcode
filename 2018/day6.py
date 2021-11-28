import re

def read_input(filename):
    f = open(filename)
    return f.readlines()

def parse_input(lines):
    pat = re.compile("(\d+), (\d+)")
    return [list(map(int, pat.match(line.strip()).groups())) for line in lines]

def min_max(seq):
    return min(seq), max(seq)

filename = "day6.txt"

input = read_input(filename)
points = parse_input(input)

min_x, max_x = min_max([tup[0] for tup in points])
min_y, max_y = min_max([tup[1] for tup in points])
