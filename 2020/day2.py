import re
from collections import namedtuple
PROBLEM_BASENAME = "day2"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)
InputRow = namedtuple("InputRow", ['policy_min',
                                   'policy_max',
                                   'policy_char',
                                   'password'])


def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.read().split("\n")
    rows = [row for row in rows if row]
    pat = re.compile("(\d+)-(\d+) (\w): (\w+)")
    data = []
    for row in rows:
        m = pat.match(row)
        g = m.groups()
        data.append(InputRow(*g))
    return data


def solve(data, check_fn):
    '''Return a list of legal passwords'''
    good_pws = []
    for row in data:
        if check_fn(row):
            good_pws.append(row)
    return good_pws

def old_valid_password(row):
    char_count = row.password.count(row.policy_char)
    if int(row.policy_min) <= char_count <= int(row.policy_max):
        return True
    

def new_valid_password(row):
    pw = row.password
    p_char = row.policy_char
    return (pw[int(row.policy_min)-1] == p_char) ^ (pw[int(row.policy_max)-1] == p_char)
