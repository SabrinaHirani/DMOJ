n = int(input())

x = 0
m = {}
r = set()
for i in range(n):
    xy = input().split()
    x1 = int(xy[1])
    x2 = int(xy[2])
    y = int(xy[0])

    for j in range(x1, x2):
        if (m.get(j) == None):
            m[j] = [ y ]
        else:
            m[j].append(y)
            m[j].sort()

    x += y*2
    r.add((x1, y))
    r.add((x2-1, y))

for i in r:
    s = m[i[0]].index(i[1])
    if (s > 0):
        x -= m[i[0]][s-1]

print(x)