PROBLEM_BASENAME = "day10"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    return([int(d) for d in data if d.isdigit()])

def solve1(data):
    prep(data)
    vals = [y-x for (x,y) in zip(data, data[1:])]
    return vals.count(1) * vals.count(3)

def solve2(data):
    count = 0
    prep(data)
    for i in data:
        
    return count

def prep(data):
    data.append(0)
    data.sort()
    data.append(3 + data[-1])
