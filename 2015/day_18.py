def read_input(filename="day_18.txt"):
    return [line_to_list(line) for line in open(filename)]


def line_to_list(line):
    line = line.strip()
    return [c == "#" for c in line]


input_data = read_input()

def iterate(grid, times=100, part_2=False):
    for _ in range(times):
        grid = compute_transition(grid, part_2=part_2)
    show_grid(grid)
    print(count_active_cells(grid))

def compute_transition(initial_grid, part_2=False):
    transition_grid = generate_transition_grid(initial_grid)
    
    result = [[compute_cell(t_cell, i_cell)
               for (t_cell, i_cell) in zip(t_row, i_row)]
              for (t_row, i_row) in zip(transition_grid, initial_grid)]
    if part_2:
        result[0][0] = True
        result[0][-1] = True
        result[-1][0] = True
        result[-1][-1] = True
        
    return result

def generate_transition_grid(initial_grid):
    transition_grid = [[0] * len(row) for row in initial_grid]
    for row_ix, row in enumerate(initial_grid):
        for col_ix, val in enumerate(row):
            if val:
                increment_neighbors(row_ix, col_ix, transition_grid)
    return transition_grid

    

def increment_neighbors(row_ix, col_ix, transition_grid):
    for i in [-1,0,1]:
        x = row_ix + i
        if 0 <= x < len(transition_grid):
            for j in [-1, 0, 1]:
                if i != 0 or j != 0:
                    y = col_ix + j
                    if 0 <= y < len(transition_grid[0]):
                        transition_grid[x][y] += 1

def compute_cell(transition_cell, initial_cell):
    if initial_cell:
        return 2<=transition_cell<=3
    else:
        return transition_cell == 3


def display_grid(grid):
    return "\n".join(["".join(["#" if cell else "." for cell in row]) for row in grid])

def show_grid(grid):
    print(display_grid(grid))

def count_active_cells(grid):
    return sum([len(list(filter(lambda x:x, row))) for row in grid])



        
    

    
example_data = """.#.#.#
...##.
#....#
..#...
#.#..#
####..""".split("\n")

example_grid = [line_to_list(line) for line in example_data]


            




