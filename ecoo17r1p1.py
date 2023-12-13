P14 = [12, 10, 7, 5]

for repeat in range(10):

    c = int(input())
    y = input().split()
    n = int(input())

    a = 0
    g = 0
    for i in range(len(y)):
        y[i] = int(float(y[i]) * n)
        if (y[i] > y[g]):
            g = i
        a += y[i]

    y[g] += (n-a)

    count = 0
    for i in range(len(y)):
        count += y[i] * P14[i]
    count /= 2

    if (count >= c):
        print('NO')
    else:
        print('YES')