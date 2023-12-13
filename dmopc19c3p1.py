x = {}
y = {}

n = int(input())
a = input().split()

for i in range(n):

    a[i] = int(a[i])

    if (x.get(a[i]) == None):
        x[a[i]] = 1
    else:
        x[a[i]] += 1

    if (y.get(x[a[i]]) == None):
        y[x[a[i]]] = set()
    y[x[a[i]]].add(a[i])

    if (x[a[i]] > 1):
        y[x[a[i]]-1].remove(a[i])

z = max(list(y.keys()))
for i in sorted(y[z]):
    print(i, end=' ')