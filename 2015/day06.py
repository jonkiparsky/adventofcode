'''
Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to
9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light. toggle 0,0
through 999,0 would toggle the first line of 1000 lights, turning off the ones
that were on, and turning on the ones that were off. turn off 499,499 through
500,500 would turn off (or leave off) the middle four lights. After following
the instructions, how many lights are lit? 
'''
from collections import defaultdict
import re

# part one functions
# def turn_on(value):
#     return 1

# def turn_off(value):
#     return 0

# def toggle(value):
#     return (value + 1) % 2


def turn_on(value):
    return value + 1

def turn_off(value):
    return max(value-1, 0)

def toggle(value):
    return value + 2


    

class Day6:
    
    year = 2015
    problem_prefix = "day6"
    pat = re.compile(r"([\w ]+) (\d+),(\d+) through (\d+),(\d+)")

    def __init__(self):
        
        self.actions = {"turn on": turn_on,
                        "turn off": turn_off,
                        "toggle": toggle}
        
        self.grid = {i: defaultdict(int) for i in range(1000)}
    
    def read_input(self):
        input_filename = "{}_input.txt".format(self.problem_prefix)
        return map(lambda s: s.strip(), open(input_filename).readlines())

    def parse_input(self, input):
        return [self.parse_line(line) for line in input]

    def parse_line(self, line, pat=None):
        pat = pat or self.pat
        m = pat.match(line)
        if not m:
            print "{} did not match pattern".format(line)
            return None
        action, x1, y1, x2, y2 = m.groups()
        p1, p2 = normalize_pair((int(x1), int(y1)), (int(x2), int(y2)))
        return {"action": self.actions[action],
                "p1": p1,
                "p2": p2}

    def solve(self, data):
        for instruction in data:
            action = instruction['action']
            p1, p2 = instruction['p1'], instruction['p2']
            for i in range(p1[1], p2[1] +1):
                row = self.grid[i]
                for j in range(p1[0], p2[0]+1):
                    row[j] = action(row[j])
        return sum([sum(row.values()) for row in self.grid.values()])

def normalize_pair(p1, p2):
    lower_left = (min(p1[0], p2[0]), min(p1[1], p2[1]))
    upper_right = (max(p1[0], p2[0]), max(p1[1], p2[1]))
    return (lower_left, upper_right)
              
    
            
            
