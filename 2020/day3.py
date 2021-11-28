PROBLEM_BASENAME = "day3"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.read().split("\n")
    rows = [row for row in rows if row]
    return rows

def solve(data, slope=(3,1)):
    tree_count = 0
    current_col = 0
    for row in data[::slope[1]]:
        tree_count += (row[current_col] == "#")
        current_col += slope[0]
        current_col %= len(row)
        
    return tree_count


def solve2(data, slopes):
    counts = [solve(data, slope=slope) for slope in slopes]
    return reduce(product, counts)

def product(x,y):
    return x*y

