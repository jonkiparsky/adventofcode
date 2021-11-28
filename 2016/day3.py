def read_input(filename="day3.txt"):
    f = open(filename)
    input = [list(map(int, line.strip().split())) for line in f]
    return input

input = read_input()


def solve_part_1(input):
    return sum([is_valid_triangle(triangle) for triangle in input])


def solve_part_2(input):
    triangles = regroup(input)
    return sum([is_valid_triangle(triangle) for triangle in triangles])
    
def is_valid_triangle(sides):
    a, b, hypotenuse = sorted(sides)
    return a + b > hypotenuse

def regroup(input):
    return chain(*[zip(*input[ix: ix+3]) for ix in range(0, len(input), 3)])


example2 = [[101, 301, 501],
            [102, 302, 502],
            [103, 303, 503],
            [201, 401, 601],
            [202, 402, 602],
            [203, 403, 603]]
