from collections import defaultdict
import re
'''
Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall.
'''

class Patch:
    def __init__(self, id, h_offset, v_offset, width, height):
        self. id = id
        self.h_offset = h_offset
        self.v_offset = v_offset
        self.width = width
        self.height = height


            
def parse_row(row):
    pat = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    m = pat.match(row)
    if not m:
        raise Exception()
    return Patch(*map(int, (m.groups())))

def parse_input(file_name):
    rows = []
    with open(file_name) as f:
        for row in f.readlines():
            rows.append(parse_row(row))
    return rows


def solve(rows):
    grid = defaultdict(int)
    for row in rows:
        for i in range(row.h_offset, row.h_offset + row.width):
            for j in range(row.v_offset, row.v_offset +  row.height):
                grid[(i, j)] += 1

    return grid

def solve2(rows):
    grid = defaultdict(list)    
    non_overlaps = set()
    for row in rows:
        non_overlaps.add(row.id)
        for i in range(row.h_offset, row.h_offset + row.width):
            for j in range(row.v_offset, row.v_offset +  row.height):
                grid[(i, j)].append(row.id)
                if len(grid[(i,j)]) > 1:
                    for id in grid[(i, j)]:
                        non_overlaps.discard(id)
    return non_overlaps
