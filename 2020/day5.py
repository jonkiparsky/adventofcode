import re
PROBLEM_BASENAME = "day5"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


table = str.maketrans("FBLR", "0101")

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.readlines()
    return [process(row) for row in rows]


def process(row):
    row = row.translate(table)
    return int(row[:7],2), int(row[7:],2)
    
    
