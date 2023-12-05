#################################################
#  Oponent
# A - rock
# B - paper
# C - scissors

#  Player
# X - rock
# Y - paper
# Z - scissors

#  Scores:
# 1 point - rock
# 2 points - paper
# 3 points - scissors
#  and
# 6 points - win
# 3 points - draw
# 0 points - lost
################################################

points = 0
points_2 = 0
WIN = (["A", "Y"], ["B", "Z"], ["C", "X"])
DRAW = (["A", "X"], ["B", "Y"], ["C", "Z"])

with open("input.txt", "r") as f:
    game = [[x for x in line.split()] for line in f.read().split("\n")]
    print(len(game))
    for round in game:
        if round in WIN: points += 6
        elif round in DRAW: points += 3
        else: points += 0
        
        for c in round:
            if c == 'X':
                points += 1
                points_2 += 0
                if round[0] == 'A': points_2 += 3
                elif round[0] == 'B': points_2 += 1
                elif round[0] == 'C': points_2 += 2
            elif c == 'Y':
                points += 2
                points_2 += 3
                if round[0] == 'A': points_2 += 1
                elif round[0] == 'B': points_2 += 2
                elif round[0] == 'C': points_2 += 3
            elif c == 'Z':
                points += 3
                points_2 += 6
                if round[0] == 'A': points_2 += 2
                elif round[0] == 'B': points_2 += 3
                elif round[0] == 'C': points_2 += 1
        print(f"Round { round }, points_v1: { points }, points_v2: { points_2 }")
f.close()

print(f"Total points in PART ONE of game: { points }")
print(f"Total points in PART TWO of game: { points_2 }")
