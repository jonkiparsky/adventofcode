def split_contents(contents):
    split_point = len(contents)//2
    return contents[:split_point], contents[split_point:]

def common_items(contents):
    c1, c2 = split_contents(contents)
    return set(c1).intersection(set(c2))

def priority(item):
    if item.islower():
        basis = "a"
        bias = 1
    else:
        basis = "A"
        bias = 27
    return ord(item) - ord(basis) + bias

def priorities(contents):
    return sum([priority(item) for item in common_items(contents)])

def solve1():
    f = open("/home/jon/code/adventofcode/2022/day3.txt")
    return sum([priorities(rucksack) for rucksack in f])

def solve2():
    f = open("/home/jon/code/adventofcode/2022/day3.txt")
    rows = [row.strip() for row in f.readlines()]
    team_size = 3
    teams = zip(*[rows[n::team_size] for n in range(team_size)])
    return sum([priority(badge(team)) for team in teams])

def badge(group):
    common = reduce(lambda a, b: a.intersection(b), map(set, group))
    return list(common)[0]
