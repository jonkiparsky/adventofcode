puzzle_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,
                31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,
                55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,
                2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,
                107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]


def process_input(input, pos):
    if input[pos] == 99:
        return False
    if input[pos] == 1:
        op1, op2, dest = input[pos+1:pos+4]
        input[dest] = input[op1] + input[op2]
        return True
    if input[pos] == 2:
        op1, op2, dest = input[pos+1:pos+4]
        input[dest] = input[op1] * input[op2]
        return True
    raise Exception

def run(input):
    cont = True
    pos = 0
    while cont:
        cont = process_input(input, pos)
        pos += 4

def part2_try(input, noun, verb):
    local_in = input[:]
    local_in[1] = noun
    local_in[2] = verb
    run(local_in)
    return local_in[0]
