from collections import defaultdict
input_file = "day7_input.txt"



class Node(object):
    
    def __init__(self, name, **kwargs):
        self.name=name
        self.__dict__.update(kwargs)
        self.parent = None
        self._total_weight = None

    def __repr__(self):
        return "Node <%s> (%d)" % (self.name, self.weight)


graph = {}

def read_input(input_file, graph):
    with open(input_file) as file:
    
        for line in file:
            data, name = line.strip().split(" -> ")
            graph[name] = data

    return graph
    
graph = read_input(input_file, graph)
    
def _and(op1, op2):
    return op1 & op2

def _or(op1, op2):
    return op1 | op2

def _lshift(op1, op2):
    return op1 << op2

def _rshift(op1, op2):
    return op1 >> op2

operators = {
    'AND': _and,
    'OR': _or,
    'LSHIFT': _lshift,
    'RSHIFT': _rshift
    }

def val(node, graph):
#    import pdb; pdb.set_trace()    
    print("entering val, " + node)
    if node.isdigit():
        return int(node)
    data = graph[node]
    if isinstance(data, int):
        return data
    if data.isdigit():
        graph[node] = int(data)
        return graph[node]
    items = data.split(" ")
    if len(items) == 1:
        graph[node] == val(items[0], graph)
        return graph[node]
    if len(items) == 2:
        assert items[0] == "NOT"
        return 65535 ^ val(items[1], graph)
    operator = items[1]
    fn = operators[operator]
    op1 = val(items[0], graph)
    graph[items[0]] = op1
    op2 = val(items[2], graph)
    graph[items[2]] = op2
    graph[node] =  fn(op1, op2)
    return graph[node]
