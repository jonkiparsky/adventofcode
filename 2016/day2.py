def read_input(filename="day2.txt"):
    f = open(filename)
    return [line.strip() for line in f]

input = read_input()

moves = {"U": (-1, 0),
         "R": (0, 1),
         "D": (1, 0),
         "L": (0, -1)}
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

 
keypad2 = [["", "",  "",  "",  "",  "",  ""],
           ["", "",  "",  "1", "",  "",  ""],
           ["", "",  "2", "3", "4", "",  ""],
           ["", "5", "6", "7", "8", "9", ""],
           ["", "",  "A", "B", "C", "",  ""],
           ["", "",  "",  "D",  "", "",  ""],
           ["", "",  "",  "",  "",  "",  ""]]

def solve_part_1(input):
    code = []
    current = (1,1)
    for line in input:
        current = solve_line(line, current)
        code.append(current)
    
    return code_to_string(code, keypad=keypad)


def move1(current, move):
    return [in_range(pos + mov) for (pos, mov) in zip(current, move)]

def solve_line(line, current, move_fn=move1):

    for c in line:
        move = moves[c]
        current = move_fn(current, move)
    return current

def solve_part_2(input):
    code = []
    current = (3,1)
    for line in input:
        current = solve_line(line, current, move_fn=move2)
        code.append(current)
    return code_to_string(code, keypad=keypad2)

def move2(current, move):
    
    y,x = [(pos + mov) for (pos, mov) in zip(current, move)]
    if keypad2[y][x]:
        return (y,x)
    else:
        return current

def in_range(x):
    if x < 0 :
        return 0
    if x >2:
        return 2
    return x
    

def code_to_string(code, keypad=keypad):
    return "".join([str(keypad[x][y]) for (x, y) in code])
        
