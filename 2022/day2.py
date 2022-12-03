"""The winner of the whole tournament is the player with the highest score. Your
total score is the sum of your scores for each round. The score for a single
round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3
for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if
the round was a draw, and 6 if you won).
"""

player_moves =  {"X": 1, "Y": 2, "Z": 3}
opponent_moves =  {"A": 1, "B": 2, "C": 3}


# player:
# X = rock, Y = paper, Z = scissors

#opponent:
# A = rock, B = paper, Z = scissors

def round_result(you, opponent):
    num_result = (player_moves[you] - opponent_moves[opponent]) % 3
    if num_result == 1:
        return 6
    if num_result == 0:
        return 3
    if num_result == 2:
        return 0

def round_score(opponent, you):
    shape_score = player_moves[you]
    return shape_score + round_result(you, opponent)

def solve1():
    f = open("/home/jon/code/adventofcode/2022/day2.txt")
    return sum([round_score(*row.strip().split(" ")) for row in f])

results_map = {"X": 2, "Y": 0, "Z": 1}

choice_map = {0: "X", 1: "Y", 2: "Z"}
def choose_move(opponent, desired):
    opponent_move_num = opponent_moves[opponent] - 1
    your_choice = (opponent_move_num + results_map[desired]) % 3
    return choice_map[your_choice]

def solve2():
    f = open("/home/jon/code/adventofcode/2022/day2.txt")
    total = 0
    for row in f:
        opp_move, desired_result = row.strip().split(" ")
        your_move = choose_move(opp_move, desired_result)
        total += round_score(opp_move, your_move)
    return total
