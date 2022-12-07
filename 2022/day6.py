f = open("/home/jon/code/adventofcode/2022/day6.txt")

def solve(text, n):
    for i in range(n, len(text)):
        block = text[i-n:i]
        if len(set(block)) == n:
            return i, block




assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)[0] == 5
assert solve("nppdvjthqldpwncqszvftbrmjlhg", 4)[0] == 6
assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)[0] == 10
assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)[0] ==  11

assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)[0] == 23
assert solve("nppdvjthqldpwncqszvftbrmjlhg", 14)[0] == 23
assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)[0] == 29
assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)[0] ==  26
