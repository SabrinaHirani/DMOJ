n = int(input())

stones = input().split()
stones = [int(x) for x in stones]

cost = [0]*n
cost[1] = abs(stones[1]-stones[0])

for i in range(2, n):
    cost[i] = min(cost[i-1]+abs(stones[i]-stones[i-1]), cost[i-2]+abs(stones[i]-stones[i-2]))

print(cost[n-1])
