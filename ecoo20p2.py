T = int(input())
for repeat in range(T):

    item = {}

    n = int(input())
    for i in range(n):
        m = int(input())
        for j in range(m):
            next = input().split()
            if (item.get(next[0]) == None):
                item[next[0]] = [[int(next[1]), int(next[2])]]
            else:
                item[next[0]].append([int(next[1]), int(next[2])])
                item[next[0]].sort(key=lambda x: x[0])

    count = 0
    k = int(input())
    for i in range(k):
        next = input().split()
        next[1] = int(next[1])
        while (next[1] > 0):
            x = item[next[0]].pop(0)
            if (x[1] > next[1]):
                x[1] = next[1]
            count += x[1] * x[0]
            next[1] -= x[1]

    print(count)