f = []
for i in range(3):
    f.append(int(input()))
limit = int(input())

c = set()
for i in range(3):
    for j in range((limit//f[i])+1):
        for k in range(((limit-(j*f[i]))//f[(i+1)%3])+1):
            for l in range(((limit-(j*f[i])-(k*f[(i+1)%3]))//f[(i+2)%3])+1):
                r = [j, k, l]
                c.add((r[(0-i)%3], r[(1-i)%3], r[(2-i)%3]))
c.remove((0, 0, 0))

for next in c:
    print('{0} Brown Trout, {1} Northern Pike, {2} Yellow Pickerel'.format(next[0], next[1], next[2]))
print('Number of ways to catch fish:', len(c))