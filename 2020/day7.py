PROBLEM_BASENAME = "day7"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)
import re
from collections import defaultdict

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.readlines()
    return [process(row.strip()) for row in rows]


def process(row):
    row = row.replace(".", "")
    row = row.split(" bags contain ")
    subject, rule = row[0], row[1]
    if rule == "no other bags":
        return subject, {}
    rule = rule.split(", ")
    pat = re.compile("(\d) (\w+ \w+) bags?")
    rule = [pat.match(piece).groups() for piece in rule]
    rule = [(piece[1], int(piece[0])) for piece in rule]
    rule = dict(rule)
    return subject, rule


def solve1(data):
    graph = build_graph(data)
    target = "shiny gold"
    del(graph[target])  # need to have at least one containing bag
    return sum([1 for key in graph.keys() if dfs(graph, key, target)])
    
def dfs(graph, start, target):
    seen = set()
    nodes = set(graph[start])
    while nodes:
        current = nodes.pop()
        if current in seen:
            continue
        seen.add(current)
        if current == target:
            return True
        nodes.update(graph[current])
    return False

def build_graph(data):
    graph = defaultdict(set)
    for row in data:
        graph[row[0]].update(row[1].keys())
        
    return graph

def build_graph2(data):
    graph = defaultdict(dict)
    for row in data:
        graph[row[0]].update(row[1])
    return graph

def graph_sum(graph, start):
    sum = 0
    for node, count in graph[start].items():
        sum += count
        sum += count * graph_sum(graph, node)
    return sum

sample = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")

sample_data = [process(row) for row in sample]
sample_graph = build_graph(sample_data)

print (solve1(sample_data))

sample2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split("\n")

sample_data2 = [process(row) for row in sample2]
sample_graph2 = build_graph2(sample_data2)
