together = {}
separate = {}
count = 0

X = int(input())
for i in range(X):
    names = input().split()
    if names[0] not in together:
        together[names[0]] = set()
    together[names[0]].add(names[1])

Y = int(input())
for i in range(Y):
    names = input().split()
    if names[0] not in separate:
        separate[names[0]] = set()
    separate[names[0]].add(names[1])

G = int(input())
for i in range(G):
    names = set(input().split())

    for name in names:
        if (name in together):
            count += len(together[name])-len(together[name].intersection(names))
        
        if (name in separate):
            count += len(separate[name].intersection(names))

print(count)

