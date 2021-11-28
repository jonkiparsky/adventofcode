PROBLEM_BASENAME = "day1"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    return([int(d) for d in data if d.isdigit()])


def solve(data, target=2020):
    head = 0
    tail = len(data) -1
    data= sorted(data)
    while head < tail:
        while data[head] + data[tail] > target:
            tail -= 1
        while data[head]+ data[tail] < target:
            head += 1
        if data[head] + data[tail] == target:
            return data[head], data[tail]



        
def solve2(data, target=2020):
    data = sorted(data)
    for i in range(len(data)):
        solution = solve(data[i+1:], target=target-data[i])
        if solution:
            return solution + (i,)
