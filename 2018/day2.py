from collections import Counter
'''
To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
'''
def parse_input(filename):
    with open(filename) as f:
        return f.readlines()


    
    
def solve(input):
    duos = 0
    trios = 0
    for box_id in input:
        counts = Counter(box_id)
        if 2 in counts.values():
            duos += 1
        if 3 in counts.values():
            trios +=1
    return duos * trios

def solve2(input):
    input = sorted(input)
    counts = {}
    for s1, s2 in zip(input, input[1:]):
        diff = compare_pairs(s1, s2)
        counts[len(diff)] = counts.get(len(diff), 0) + 1
        if len(diff) == 1:
            pos = diff[0]
            return s1[:pos] + s1[pos+1:]
#        print s1, s2, diff
    return counts

def compare_pairs(s1, s2):
    diffs = []
    for i, pair in enumerate(zip(s1, s2)):
        if pair[0] != pair[1]:
            diffs.append(i)
    return diffs
