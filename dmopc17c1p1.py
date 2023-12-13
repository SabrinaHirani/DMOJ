import sys
input = sys.stdin.readline

rc = input().split()
r = int(rc[0])
c = int(rc[1])

x = [False for a in range(c+1)]
y = [False for a in range(r+1)]

for i in range(r):
    next = input()
    for j in range(c):
        if (next[j] == 'X'):
            x[j+1] = True
            y[i+1] = True

q = int(input())
for i in range(q):
    next = input().split()
    if (x[int(next[0])] or y[int(next[1])]):
        print('Y')
    else:
        print('N')