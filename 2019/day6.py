def read_data(filename="day6.txt"):
    f = open(filename)
    return [l.strip().split(")") for l in f]


def build_graph(data):
    orbits = defaultdict(list)
    for (a, b) in data:
        orbits[a].append(b)
    return orbits

def visit(node, data, depth):
    return depth + sum([visit(child, data, depth + 1) for child in data[node]])


def map_graph(graph, current_node, current_path, paths):
    current_path = current_path + [current_node]
    paths[current_node] = current_path
    for node in graph[current_node]:
        map_graph(graph, node, current_path, paths)
    return paths


def find_divergence_point(this, that, paths):
    '''Return the index of the last common node on paths to
    _this_ and _that_'''
    this_path, that_path = paths[this], paths[that]
    for (ix, (i, j)) in enumerate(zip(this_path, that_path)):
        if i != j:
            return ix-1

def compute_transfer_count(this, that, paths):
    divergence_point = find_divergence_point(this, that, paths)
    this_path = paths[this]
    that_path = paths[that]
    return len(this_path) + len(that_path) - 4 - (2 * divergence_point)
