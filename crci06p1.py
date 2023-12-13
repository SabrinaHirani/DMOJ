n = int(input())
e = int(input())

m = {}

for i in range(e):

    next = input().split()[1:]

    if ('1' in next):
        for j in range(len(next)):

            next[j] = int(next[j])

            if (m.get(next[j]) == None):
                m[next[j]] = set()
            m[next[j]].add(i)
    else:
        x = set()
        for j in range(len(next)):

            next[j] = int(next[j])

            if (m.get(next[j]) != None):
                x.update(m[next[j]])

        for j in range(len(next)):
             m[next[j]] = x.copy()

for j in sorted(list(m.keys())):
    if (len(m[j]) == len(m[1])):
        print(j)