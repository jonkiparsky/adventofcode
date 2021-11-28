from collections import Counter

import re

ORD_A = ord("a")
pat = re.compile(r"((\w+-)+)(\d+)\[(\w+)\]")

def read_input(filename="day4.txt"):
    f = open(filename)
    return [process_line(line) for line in f]


input = read_input()

def process_line(line):
    m = pat.match(line.strip())
    room_id, _, sector_id, checksum = m.groups()
    return (room_id, int(sector_id), checksum)
        

def solve_part_1(input):
    total = 0
    for room_id, sector_id, checksum in input:
        if is_a_real_room(room_id, checksum):
            total += sector_id
    return total

def is_a_real_room(room_id, checksum):
    # 
    # True iff checksum == 5 most-common letters in room_id,
    # ties broken alphabetically

    letters = room_id.replace("-", "")
    counted = [tup for tup in Counter(letters).items()]
    counted.sort(key=itemgetter(0))
    counted.sort(key=itemgetter(1), reverse=True)

    expected_checksum = "".join([t[0] for t in counted[:5]])
    return expected_checksum == checksum

def decrypt(room_id, sector_id):
    return " ".join([rotate_word(word, sector_id) for word in room_id.split("-")])
                    

def rotate_word(word, n):
    return "".join([rotate_char(char, n) for char in word])

def rotate_char(char, n):
    ix = ord(char) - ORD_A
    new_ix = (ix + n) % 26
    return chr(new_ix + ORD_A)


def solve_part_2(input):
    decrypted = []
    for (room_id, sector_id, checksum) in input:
        if is_a_real_room(room_id, checksum):
            decrypted.append((decrypt(room_id, sector_id), sector_id))
    return decrypted
