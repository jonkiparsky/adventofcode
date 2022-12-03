sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def solve(lines):
    current = 0
    max_seen = 0

    for line in lines:
        if line.strip() == "":
            current = 0
        else:
            current += int(line)
            max_seen = max(max_seen, current)
    return max_seen

def solve2(lines):
    current = 0
    totals = []
    for line in lines:
        if line.strip() == "":
            totals.append(current)
            current = 0

        else:
            current += int(line)
    if current:
        totals.append(current)
    return sorted(totals)[-3:]
