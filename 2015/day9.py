from collections import namedtuple
import re

pat = re.compile("(\w+) to (\w+) = (\d+)\n?")
Edge = namedtuple("Edge", ['ends', 'length'])
Node = namedtuple("Node", ['name', 'adjacencies'])
Adjacency = namedtuple("Adjacency", ['destination', 'length'])


def parse_input(input):
    edges = []
    nodes = set()
    for line in input:
        p1, p2, len = pat.match(line).groups()
        edges.append(Edge((p1, p2), int(len)))
        nodes.update((p1,p2))
    return edges, {name: Node(name, {}) for name in nodes}


def construct_graph(edges, nodes):
    for ends, length in edges:
        p1, p2 = ends
        nodes[p1].adjacencies[p2] = length
        nodes[p2].adjacencies[p1] = length
    return nodes

def tsp_search(graph, nodes):
    return _tsp_helper(graph, list(nodes), 0)

def _tsp_helper(graph, nodes, path_len):
    if len(nodes) == 0:
        return path_len
    next_node = nodes[0]

    

def path_length(path, graph):
    return sum([dist(p1, p2, graph)
                for p1, p2 in zip(path, path[1:])])

def dist(p1, p2, graph):
    return graph[p1].adjacencies[p2]


    
