from collections import defaultdict

def read_input(filename="day1.txt"):
    f = open(filename)
    return f.read().strip().split(", ")


input = read_input()

directions = [(0,1),(1,0), (0,-1), (-1,0)]  # North, East, South, West
turns = {"L": -1, "R": +1}

def turn(current_orientation, turn_direction):
    # orientation is an index into `directions`, 0..3
    return (current_orientation + turns[turn_direction]) % 4


def travel(location, orientation, distance):
    direction = directions[orientation]
    return tuple([loc + dir * distance for loc, dir in zip(location, direction)])

def travel_2(location, orientation, distance, map):
    direction = directions[orientation]
    for i in range (1, distance + 1):
        grid_point = tuple([loc + dir * i for loc, dir in zip (location, direction)])
        if grid_point in map:
            return grid_point, True
        map[grid_point] = 1
    return grid_point, False
    
def solve_part_1(input):
    orientation = 0
    location = (0,0)
    
    for step in input:
        turn_direction = step[0]
        distance = int(step[1:])
        orientation = turn(orientation, turn_direction)
        location = travel(location, orientation, distance)
    return sum(map(abs, location))

def solve_part_2(input):
    orientation = 0
    location = (0,0)
    map = {location: 1}
    for step in input:
        turn_direction = step[0]
        distance = int(step[1:])
        orientation = turn(orientation, turn_direction)
    
        location, result = travel_2(location, orientation, distance, map)
        if result:
            return location
        else:
            location = location
