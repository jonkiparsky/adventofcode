import re

PROBLEM_BASENAME = "day12"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)

pat = re.compile("(\w)(\d+)")

origin = (0,0)
east = (1,0)

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    
    return [process(row) for row in data if row]

def process(row):
    action, arg =  pat.match(row).groups()
    return action, int(arg)


def forward(position, orientation, distance):
    new_pos = tuple([pos + o * distance for pos, o in zip (position, orientation)])
    return new_pos, orientation

def move_fn(direction):
    def fn(position, orientation, distance):
        new_pos = tuple([pos + d * distance for pos, d in zip (position, direction)])
        return new_pos, orientation
    return fn

def turn_fn(rotation):
    orientations = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    def fn(position, orientation, degrees):
        delta_ix = rotation * (degrees//90)
        original_ix = orientations.index(orientation)
        new_ix = (original_ix + delta_ix) % 4
        return position, orientations[new_ix]
    return fn

actions = {
    "N": move_fn((0, 1)),
    "S": move_fn((0, -1)),
    "E": move_fn((1, 0)),
    "W": move_fn((-1, 0)),
    "L": turn_fn(1),
    "R": turn_fn(-1),
    "F": forward
}

def execute_instruction(position, orientation, instruction):
    action, arg = instruction
    fn = actions[action]

    new_pos, new_or =  fn(position, orientation, arg)
    print (instruction, new_pos, new_or)
    return new_pos, new_or


def manhattan_dist(position):
    return sum([abs(x) for x in position])

        
sample_data = """F10
N3
F7
R90
F11""".split("\n")

#instructions = [process(row) for row in sample_data]

instructions = parse_input()

position = origin
orientation = east


for action, arg in instructions:
    fn = actions[action]
    position, orientation = fn(position, orientation, arg)


print (position, orientation)

def west(position, orientation, distance):
    direction = (-1, 0)
    new_pos = tuple([pos + d * distance for pos, d in zip (position, direction)])
    return new_pos, orientation
