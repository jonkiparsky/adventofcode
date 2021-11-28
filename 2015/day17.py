input = '''50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40'''.split("\n")

input = sorted([int(i) for i in input], reverse=True)

def solve_part_1(input):
    input = input.copy()
    return len(recursive_solve_1(150, input, []))
               
from collections import Counter
def solve_part_2(input):
    results = recursive_solve_1(150, input, [])
    c = Counter([len(s) for s in results])
    return c[min(c.keys())]
                
def recursive_solve_1(quantity, containers, prefix):
    if quantity == 0:
        return [prefix]
    if not containers:
        return []
    result = []
    if quantity >= containers[0]:
        car, cdr = containers[0], containers[1:]
        result.extend(recursive_solve_1(
            quantity - car,
            cdr,
            prefix + [car]))
    result.extend(recursive_solve_1(
        quantity,
        containers[1:],
        prefix))
    return result
                       
            
            
