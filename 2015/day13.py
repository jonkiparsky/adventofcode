
import re
sign = {'gain': 1,
        'lose': -1}
pat = re.compile("(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")

def parse_input(input):
    guests = defaultdict(dict)
    for line in input:
        m = pat.match(line)
        guest1, polarity, amount, guest2 = m.groups()
        guests[guest1][guest2] = sign[polarity] * int(amount)
    return guests   

def pairwise_prefs(data):
    prefs = {}
    for n1 in data.keys():
        for n2 in data[n1].keys():
            prefs[tuple(sorted([n1, n2]))] = data[n1][n2] + data[n2][n1]
    return prefs

def recursive_solve(preferences, names, total=0, result=None):
    
    if result is None:
        result = []
    if not preferences:
        return result, total
    if all([(result.count(name) == 2) for name in names]):
        return result, total
    my_preferences = preferences[:]
    curr_pair, curr_val = my_preferences.pop()
    while (result.count(curr_pair[0]) >= 2 or
           result.count(curr_pair[1]) >= 2) and my_preferences:
        curr_pair, curr_val = my_preferences.pop()
    if not my_preferences:
        return ([], 0)
    return max((recursive_solve(my_preferences, names, total+curr_val, result+list(curr_pair)),
                recursive_solve(my_preferences, names, total, result)),
               key = lambda t:t[1])
    
            
            
