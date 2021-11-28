from collections import Counter

'''
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 130254-678275
'''
input = (130254, 678275)

new_max = 677999
new_min = 133333

def test(i):
    digits = list(str(i))
    if sorted(digits) != digits:
        return 0
    if any([i==j for i, j in zip(digits, digits[1:])]):
        return 1
    return 0

def test2(i):
    digits = list(str(i))
    if sorted(digits) != digits:
        return 0
    if 2 in Counter(digits).values():
        return 1
    return 0

def brute_solve(low, high, test_fn):
    found = 0
    for i in range(low, high + 1):
        found += test_fn(i)
        if i % 10000 == 0:
            print (i, found)
    print (found)





