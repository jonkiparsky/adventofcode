from collections import Counter


def read_input(filename="day6.txt"):
    f = open(filename)
    return [line.strip() for line in f]

input = read_input()

def solve1(input):
    cols = list(zip(*input))
    counts = [Counter(col) for col in cols]
#    tops = [sorted(counted.items(), key=lambda t:t[1])[-1] for counted in counts]
    tops = [sorted(counted.items(), key=lambda t:t[1])[0] for counted in counts]    
    
    return [val for (val, _) in tops]
