nd = input().split()
n = int(nd[0])
d = int(nd[1])

sum = 0
ps = []
p = input().split()
for i in range(n):
    p[i] = int(p[i])
    sum += p[i]
    ps.append(sum)

for i in range(d):
    next = int(input())

    if (ps[next-1] >= (ps[-1]-ps[next-1])):
        print(ps[next-1])
        x = ps[next-1]
        ps = ps[next:]
        for j in range(len(ps)):
            ps[j] -= x

    else:
        print(ps[-1]-ps[next-1])
        ps = ps[:next]