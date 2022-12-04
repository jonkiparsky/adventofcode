import re

input_file = "/home/jon/code/adventofcode/2022/day4.txt"

input_pattern = re.compile("(\d+)-(\d+),(\d+)-(\d+)")

def parse_row(row):
    a, b, c, d = map(int, input_pattern.match(row).groups())
    return (a, b), (c, d)

def parse_input(rows):
    return [parse_row(row) for row in rows]


def range_contains_subrange(pair_of_ranges):
    r1, r2 = sorted(pair_of_ranges)
    if r1[0] == r2[0]:
        return True
    return r1[1] >= r2[1]

def solve1():
    f = open(input_file)
    data = parse_input(f.readlines())
    return sum([1 for row in data if range_contains_subrange(row)])

def range_overlaps_range(pair_of_ranges):
    r1, r2 = sorted(pair_of_ranges)
    return r1[1] >= r2[0]

def solve2():
    f = open(input_file)
    data= parse_input(f.readlines())
    return sum([1 for row in data if range_overlaps_range(row)])
