import sys
input = sys.stdin.readline

nk = input().split()
n = int(nk[0])
k = int(nk[1])

stones = input().split()
stones = [int(x) for x in stones]

cost = [0]*n
for i in range(1, n):
    cost[i] = min([cost[i-j]+abs(stones[i-j]-stones[i]) for j in range(1, min(i, k)+1)])

print(cost[n-1])
