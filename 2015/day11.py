input = "hepxcrrq"
Z = ord("z")
A = ord("a")

def solve(input):
    while not(test(input)):
        input = increment(input)
    return input

def test(input):
    if any([i in input for i in ["i", "l", "o"]]):
        return False
    if not test_pairs(input, 2):
        return False
    if not test_ascending_sequence(input):
        return False
    return True

def test_pairs(input, qty):
    matched = []
    for i, j in zip(input, input[1:]):
        if i == j and i not in matched:
            matched.append(i)
            qty -= 1
            if qty == 0:
                return True
    return False

def test_ascending_sequence(input):
    input = map (ord, input)
    for i, j, k in zip(input, input[1:], input[2:]):
        if i == j-1 == k-2:
            return True
    return False

def increment(s):
    ords = map(ord, s)
    ords[-1] += 1
    ords = resolve_carry(ords)
    return "".join(map(chr, ords))

def resolve_carry(ords):
    carry = False
    result = []
    for i in reversed(ords):
        if carry:
            i+=1
        carry = False
        if i > Z:
            i = A
            carry = True
        result.insert(0, i)
    return result
