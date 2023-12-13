for repeat in range(10):

    nt = input().split()
    t = int(nt[0])
    n = int(nt[1])

    q = 0
    for i in range(n):

        b = input()
        if (b == 'B'):
            q += t

        if (q > 0):
            q -= 1

    print(q)