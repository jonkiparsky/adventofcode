from collections import defaultdict
from math import sqrt


def solve(lim):
    cells = defaultdict(int)
    max_val = 1
    i = 2
    for j in range(1, 10):
        cells[j]=1
    
    while True:
        touch(i, cells)
        if cells[i] > lim:
            return cells, i
        i += 1
        if i % 100 == 0:
            return cells, i

def touch(i, cells):
    val = cells[i]
    for n in neighbors(i):
        cells[n] += val
    


def neighbors(i):
    # do a bit of case analysis and solve each case separately
    if i == 2:
        return [3,4,8,9,10,11,12]
    n = int_root(i)

    if is_square(i) or is_square(i-n):
        return almost_corner(i)
    elif is_square(i-1) or is_square(i+n):
        return corner(i)
    else:
        return plain_edge(i)


def almost_corner(i):
    # in this case, we need i+1 and i+2 as well as the outside neighbors
    return [corner_outside(i+1) - j for j in range(1, 4)] + [i+1, i+2]

def corner(i):
    # for a corner, we have five neighbors outside, plus the successor of i
    outside_corner = corner_outside(i)
    return [outside_corner + x for x in range(-2, 3)] + [i+1]
    
def plain_edge(i):
    # in this case, we want to get our offset from the corner prior
    # and the corner "outside" from that corner. We can then calculate
    # our outer neighbors trivially.

    prior_corner = corner_below(i)
    offset = i - prior_corner
    first_outside_neighbor = corner_outside(prior_corner) + offset
    return [first_outside_neighbor + i for i in range(3)] + [i+1]
    
def is_square(n):
    return int_root(n) ** 2 == n

def int_root(n):
    return int(sqrt(n))


def corner_below(i):
    # the corner below is either the greatest square+1 less than i
    # or the corner between that and the square above i

    square_below = int_root(i) ** 2
    square_above = ( int_root(i) + 1 ) ** 2
    if i - square_below < square_above - i:
        return square_below + 1

    else:
        return square_above - int_root(i)

def corner_outside(i):
    # the corner outside i is either the square of (int_root(i) + 2) + 1
    # or (int_root(i) + 2)**2 + int_root(i) + 2 + 1 depending on which axis we're on
    square_below = int_root(i) ** 2
    square_above = ( int_root(i) + 1 ) ** 2
    if i - square_below < square_above - i:
        return (int_root(i) + 2) ** 2 + 1
    else:
        return (int_root(i) + 2) ** 2 + int_root(i) + 3
    
