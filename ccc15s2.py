J = int(input())
A = int(input())

conversion = {'S': 0, 'M': 1, 'L': 2}

sizes = []
for i in range(J):
    s = conversion[input()]
    sizes.append(s)

count = 0
for i in range(A):
    sn = input().split()
    s = conversion[sn[0]]
    n = int(sn[1])-1
    if s <= sizes[n]:
        sizes[n] = -1
        count += 1

print(count)