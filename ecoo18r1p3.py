for repeat in range(10):
    nxyz = input().split()
    n = int(nxyz[0])
    x = int(nxyz[1])
    y = int(nxyz[2])
    z = int(nxyz[3])

    code = []
    for i in range(n):
        next = list(input())
        for j in range(len(next)):
            next[j] = int(next[j])
            if (next[j] == 0):
                next[j] = str(z)
            elif (next[j]%2 == 0):
                next[j] = str(next[j]+x)
            else:
                next[j] = str(max(next[j]-y, 0))
        code.append(''.join(next))

    input()
    fail = []
    for i in range(n):
        if (input() != code[i]):
            fail.append(str(i+1))
    input()

    if (len(fail) == 0):
        print('MATCH')
    else:
        print('FAIL:', ','.join(fail))