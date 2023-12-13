n = int(input())

for i in range(n):

    d = set()
    next = int(input())

    for i in range(1, next//2):
        if ((next//i) == (next/i)):
            d.add(i)
            if (i != 1):
                d.add(next//i)

    count = sum(d)
    if (count == next):
        print(next, 'is a perfect number.')
    elif (count > next):
        print(next, 'is an abundant number.')
    else:
        print(next, 'is a deficient number.')