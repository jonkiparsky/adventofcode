PROBLEM_BASENAME = "day9"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    return([int(d) for d in data if d.isdigit()])

def solve1(data, prefix_length=25):
    for i in range(prefix_length, len(data)):
        if not check(data, i, prefix_length):
            return data[i]

    return "oops"

def check(data, ix, prefix_length=25):
    prefix = data[ix-prefix_length:ix]
    return any([data[ix] - x in prefix for x in prefix if data[ix] != 2 * x])



def solve2(data,target = 27911108):
    i, k = 0,1
    contiguous_sum = data[i] + data[k]
    while True:
        print (contiguous_sum, i, k, data[i], data[k])
#        import pdb; pdb.set_trace()

        if contiguous_sum == target:
            return max(data[i:k+1]) + min(data[i:k+1])
 
        if contiguous_sum < target:
            k+=1
            contiguous_sum+=data[k]
        if contiguous_sum > target:
            contiguous_sum -= data[i]            
            i+=1






def subarrays(data, target):
    subs = [[]]
    current = subs[0]
    for i in data:
        if i < target:
            current.append(i)
        else:
            if current:
                current = []
                subs.append(current)
    return subs




sample_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")
sample_data = list(map(int, sample_data))
#print(solve1(sample_data, prefix_length=5))
