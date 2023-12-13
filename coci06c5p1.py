moves = input()

pos = 1
for move in moves:
    if (move == 'A'):
        if (pos == 1):
            pos = 2
        elif (pos == 2):
            pos = 1
    elif (move == 'B'):
        if (pos == 2):
            pos = 3
        elif (pos == 3):
            pos = 2
    elif (move == 'C'):
        if (pos == 1):
            pos = 3
        elif (pos == 3):
            pos = 1

print(pos)