import re
from collections import defaultdict
from itertools import chain

template = "Step (\w) must be finished before step (\w) can begin."

pat = re.compile(template)

def read_input(filename):
    with open (filename) as f:
        return map(lambda l:l.strip(), f.readlines())
    
def parse_input(lines):
    nodes = [pat.match(line).groups() for line in lines]
    return nodes


def calc_duration(label, base_time):
    return base_time + ord(label) - ord("A") 
    
class Task:
    def __init__(self, label, base_time=60):
        self.label = label
        self._unvisited_predecessor_count = 0
        self.predecessors = []
        self.successors = []
        self.duration = calc_duration(label, base_time)
        self.started = False

    def start(self):
        self.started = True

    def complete(self, tasks):
        for successor in self.successors:
            successor.predecessor_visited()
        tasks.append(self)
        
    def predecessor_visited(self):
        self._unvisited_predecessor_count -= 1

    def __str__(self):
        return self.label

    def __repr__(self):
        return "<Node: %s>" % self.label

class Worker:
    def __init__(self, id_no):
        self.id = id_no
        self.task = None
        self.time_remaining = 0
        
    def assign(self, task):
        self.task = task
        if task:
            self.time_remaining = task.duration
            task.start()

    def complete_task(self, tasks):
        self.task.complete(tasks)
        self.task = None
        
    def tick(self, vqueue, tasks):
        if self.task is not None:
            if self.time_remaining > 0:
                self.time_remaining -= 1
            else:
                self.complete_task(tasks)
        if self.task is None:
            self.assign(vqueue.next())

    def __repr__(self):
        return "<Worker %d>" % self.id
    
class VisitQueue:
    def __init__(self, node_list):
        self.items = node_list

    def add(self, item):
        self.items[item.label] = item

    def next(self):
        candidates = filter(lambda x: x._unvisited_predecessor_count==0,
                            self.items.values())
        candidates = filter(lambda c: not c.started, candidates)
        if candidates:
            n = sorted(candidates, key=lambda l:l.label)[0]
            self.items.pop(n.label)
            return n
        return None

        

def make_nodes(edge_list, base_time=60):
    node_labels = set(chain(*edge_list))
    return {label: Task(label, base_time) for label in node_labels}

def set_edges(node_list, edge_list):
    for pred, succ in edge_list:
        node_list[pred].successors.append(node_list[succ])
        node_list[succ].predecessors.append(node_list[pred])
        node_list[succ]._unvisited_predecessor_count += 1

        



sample_input = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip().split("\n")

def solve(input, base_time=60, worker_count=5):
    edges = parse_input(input)
    nodes = make_nodes(edges, base_time=base_time)
    set_edges(nodes, edges)
    vq = VisitQueue(nodes)
    tasks = []
    workers = [Worker(i) for i in range(worker_count)]
    item_count = len(nodes)
    time = 0
    while len(tasks) < item_count:
        time = tick(workers, vq, tasks, time)
    return time


def tick(workers, vq, tasks, time):
    print "time %d" % time    
    for worker in workers:
        worker.tick(vq, tasks)
        # print "%s: %s (%d)" % (str(worker), str(worker.task), worker.time_remaining)
        # print ", ".join([str(task) for task in tasks])
    return time + 1





# tried: 1135 (too high)
