x = list(input())

L = x.count('L')
M = x.count('M')

swap = 0
c1 = 0
c2 = 0
for i in range(L):
    if (x[i] != 'L'):
        if (x[i] == 'M'):
            c1 += 1
        swap += 1

for i in range(L, L+M):
    if (x[i] != 'M'):
        if (x[i] == 'L'):
            c2 += 1
        swap += 1

print(swap-min(c1, c2))