import re

def read_input(filename="day7.txt"):
    f = open(filename)
    return [line.strip() for line in f]

lines = read_input()
good_match = re.compile(r"(\w)(\w)\2\1")
bad_match = re.compile(r"\[\w*(\w)(\w)\2\1\w*]")

def solve1(input):
    return sum([bool(supports_TLS(line)) for line in input])


def supports_TLS(line):
    bad_match_m = bad_match.search(line)
    if bad_match_m:
        a, b = bad_match_m.groups()
        if a != b:
            return False
    good_match_m = good_match.search(line)
    if good_match_m:
        a, b = good_match_m.groups()
        return a != b



test_cases = {"abba[mnop]qrst": True,
              "abcd[bddb]xyyx": False,
              "aaaa[qwer]tyui": False,
              "ioxxoj[asdfgh]zxcvbn": True}

bracketed = re.compile(r"\[(\w*)]")

def solve2(input):
    return [line for line in input if supports_SSL(line)]


ababab = re.compile(r"(\w)(\w)\1\w*(?:\[\w*]\w*)*\[\w*\2\1\2\w*]")


bababa = re.compile(r"\[\w*(\w)(\w)\1\w*]\w*(?:\[\w*]\w*)*\2\1\2")    

def supports_SSL(line):
    if (aba_m:=ababab.search(line)):
        a, b = aba_m.groups()
        if a != b:
            return True
    if (bab_m:=bababa.search(line)):
        a, b, = bab_m.groups()
        if a != b:
            return True
    return False

examples2 = {
    "aba[bab]xyz": True, 
    "xyx[xyx]xyx": False,
    "aaa[kek]eke": True,
    "zazbz[bzb]cdb": True}


