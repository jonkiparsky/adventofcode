import re
PROBLEM_BASENAME = "day6"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


table = str.maketrans("FBLR", "0101")

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.read().strip()
    groups = rows.split("\n\n")
    return groups


def solve1(groups):
    return sum([total(group) for group in groups])

def solve(groups):
    return sum([count(group) for group in groups])

def count(group): 
    people = [set(g) for g in group.split("\n")]
    responses = people[0]
    for person in people:
        responses = responses.intersection(person)
    return len(responses)
    

def total(group):
    group = group.replace("\n", "")
    return len(set(group))
        
        

groups = parse_input()
print(solve(groups))


sample = """abc

a
b
c

ab
ac

a
a
a
a

b""".split("\n\n")
print(solve(sample))
    
