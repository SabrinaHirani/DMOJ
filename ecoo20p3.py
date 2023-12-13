T = int(input())

for repeat in range(T):

    n = int(input())
    result = ''

    for i in range(n):

        hw = input().split()
        h = int(hw[0])
        w = int(hw[1])

        grid = []
        for j in range(h):
            next = input()
            grid.append(next)

        

        off1 = 0

        v1 = ''
        for k in range(h):
            v1 += grid[k][0]

        z = 1
        while (v1 == '-'*h):
            v1 = ''
            for k in range(h):
                v1 += grid[k][z]
            off1 += 1
            z += 1



        off2 = 0

        v2 = ''
        for k in range(h):
            v2 += grid[k][-1]

        z = -1
        while (v2 == '-'*h):
            v2 = ''
            for k in range(h):
                v2 += grid[k][z]
            off2 += 1
            z -= 1



        off3 = 0

        z1 = 0
        h1 = grid[z1]
        while (h1 == '-'*w):
            z1 += 1
            off3 += 1
            h1 = grid[z1]
        z1 -= 1



        off4 = 0

        z2 = -1
        h2 = grid[z2]
        while (h2 == '-'*w):
            z2 -= 1
            off4 += 1
            h2 = grid[z2]
        z2 += 1



        h3 = grid[z1 + ((h+z2)-z1)//2]



        v1 = v1[off3 : len(v1)-(off4)]
        v2 = v2[off3 : len(v2)-(off4)]

        h1 = h1[off1 : len(h1)-(off2-1)]
        h2 = h2[off1 : len(h2)-(off2-1)]
        h3 = h3[off1 : len(h3)-(off2-1)]

        h = len(v1)
        w = len(h1)



        if (h2[-1] == '*'):

            if (v1 == v2):
                result += '1'

            elif (v1[(h//4)] == '*'):
                result += '4'

            else:
                result += '7'

        else:

            if (h3.count('*') == 0):
                result += '0'

            else:

                if (v1[h//4] != '*'):

                    if (h2[0] == '*'):
                        result += '3'
                    
                    else:
                        result += '2'

                elif (v2[h//4] != '*'):

                    if (v1[(h//2):].count('*') > 0):
                        result += '6'

                    else:
                        result += '5'

                else:

                    if (v1[(h//2):].count('*') > 0):
                        result += '8'
                    else:
                        result += '9'

    print(result)