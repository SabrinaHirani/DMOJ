n = int(input())

x = set()
m = {}

for i in range(n):
    next = input()
    if (next in x):
        if (m.get(next) == None):
            m[next] = 1
        else:
            m[next] += 1
    else:
        x.add(next)

for i in range(n-1):
    next = input()
    if (m.get(next) != None):
        m[next] -= 1
        if (m[next] == 0):
            m.pop(next)
    else:
        x.remove(next)

for i in x:
    print(i)