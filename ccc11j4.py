next = [-1, -1]
illegal = set([(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), (5, -5), (5, -4), (5, -3), (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7), (-1, -6), (-1, -5)])

h = -1
v = -5
status = 'safe'
while (next[0] != 'q'):
    next = input().split()
    next[1] = int(next[1])+1

    if ((next[0] == 'l') or (next[0] == 'r')):

        if (next[0] == 'l'):
            next[1] *= (-1)

        for x in range(h+int((next[1])/abs((next[1]))), h+(next[1]), int((next[1])/abs((next[1])))):
            if ((x, v) in illegal):
                status = 'DANGER'
            else:
                illegal.add((x, v))
            h = x
        
    elif ((next[0] == 'u') or (next[0] == 'd')):

        if (next[0] == 'd'):
            next[1] *= (-1)

        for x in range(v+int((next[1])/abs((next[1]))), v+(next[1]), int((next[1])/abs((next[1])))):
            if ((h, x) in illegal):
                status = 'DANGER'
            else:
                illegal.add((h, x))
            v = x

    else:
        break

    print(h, v, status)
    if (status == 'DANGER'):
        break