import sys
input = sys.stdin.readline

nqh = input().split()
n = int(nqh[0])
q = int(nqh[1])
h = int(nqh[2])

sum = 0
trees = [0]
for i in range(n):
    next = input().split()
    if (int(next[0]) <= h):
        sum += int(next[1])
    trees.append(sum)

max = 0
for i in range(q):
    next = input().split()
    x = trees[int(next[1])] - trees[int(next[0])-1]
    if (x > max):
        max = x
print(max)