def read_data(filename):
    f = open(filename)
    return list(map(int, f.read().strip().split(",")))
