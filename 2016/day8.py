def read_input(filename="day8.txt"):
    f = open(filename)
    return [parse_line(line) for line in f]

ROW_LEN = 50
COL_LEN = 6


def rect(screen, x, y):
    for y_ in range(y):
        for x_ in range(x):
            screen [y_][x_] = True

def rotate(screen, direction, axis, shift):
    if direction == "row":
        rotate_row(screen, axis, shift)
    else:
        rotate_col(screen, axis, shift)

def rotate_row(screen, y, shift):
    for _ in range (shift):
        screen[y].insert(0, screen[y].pop(-1))

def rotate_col(screen, x, shift):
    transposed_col = [screen[y][x] for y, _ in enumerate(screen)]
    for _ in range(shift):
        transposed_col.insert(0, transposed_col.pop(-1))
    for y, val in enumerate(transposed_col):
        screen[y][x] = val
                         

def parse_line(line):
    match line.split():
        case ["rect", dim]:
            return (rect, list(map(int, dim.split("x"))))
        case ["rotate", direction, spec, _, rotation]:
            axis_index = spec.split("=")[1]
            return (rotate, (direction, int(axis_index), int(rotation)))
        

def new_screen(row_len=ROW_LEN, col_len=COL_LEN):
    return [row_len * [False] for row in range(col_len)]

def process_instructions(parsed_lines):
    screen = new_screen()

    for fun, args in parsed_lines:
        fun(screen, *args)

    return screen
