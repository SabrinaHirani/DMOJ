kn = input().split()
k = int(kn[0])
n = int(kn[1])

words = {}
for i in range(k):
    next = input()
    if (words.get(next[0]) == None):
        words[next[0]] = [next]
    else:
        words[next[0]].append(next)
        words[next[0]].sort()

for i in range(n):
    next = input()
    x = words[next].pop(0)
    words[next].append(x)
    print(x)