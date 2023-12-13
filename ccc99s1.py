gws  = {'jack': 1, 'queen': 2, 'king': 3,'ace': 4}

a = 0
b = 0
w = 0
s = 0

for i in range(52):

    next = input()
    if (gws.get(next) != None):
        w = gws.get(next)
        s = 0

    elif (w != 0):
        w -= 1
        s += 1
        
        if (w == 0):
            if (((i%2 == 0) and (s%2 == 0)) or ((i%2 == 1) and (s%2 == 1))):
                print(f'Player A scores {s} point(s).')
                a += s
            elif (((i%2 == 0) and (s%2 == 1)) or ((i%2 == 1) and (s%2 == 0))):
                print(f'Player B scores {s} point(s).')
                b += s
            s = 0

print(f'Player A: {a} point(s).')
print(f'Player B: {b} point(s).')