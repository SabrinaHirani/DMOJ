n = int(input())

for i in range(n):

    c = []
    guesses = []

    g = int(input())

    for j in range(g):

        next = input().split()
        hint = next[1].split('/')

        guesses.append([next[0], int(hint[0]), int(hint[1])])
        
    for j in range(9999+1):

        next = ((4-len(str(j)))*'0') + (str(j))
        copy = next

        for k in range(len(guesses)):

            next = copy
            compare = guesses[k][0]

            c1 = 0
            for h in range(4):
                if (next[h] == compare[h]):
                    if (h == 3):
                        next = next[:h] + '*'
                        compare = compare[:h] + '?'
                    else:
                        next = next[:h] + '*' + next[h+1:]
                        compare = compare[:h] + '?' + compare[h+1:]
                    c1 += 1
            
            if (c1 != guesses[k][1]):
                break

            c2 = 0
            for h in range(4):
                if ((compare[h] in next) and (next[h] != compare[h])):

                    idx = next.index(compare[h])
                    if (idx == 3):
                        next = next[:idx] + '*'
                    else:
                        next = next[:idx] + '*' + next[idx+1:]

                    if (h == 3):
                        compare = compare[:h] + '?'
                    else:
                        compare = compare[:h] + '?' + compare[h+1:]

                    c2 += 1
            
            if (c2 != guesses[k][2]):
                break

            if (k == len(guesses)-1):
                c.append(copy)

    if (len(c) == 1):
        print(c[0])
    elif (len(c) == 0):
        print('impossible')
    else:
        print('indeterminate')