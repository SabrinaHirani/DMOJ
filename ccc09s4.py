import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

t = int(input())
for i in range(t):
    xyc = input().split()
    x = int(xyc[0])
    y = int(xyc[1])
    c = int(xyc[2])
    if x <= n and y <= n:
        graph[x][y] = c
        graph[y][x] = c

cost = [float('inf')] * (n+1)
priority_queue = []
k = int(input())
for i in range(k):
    zp = input().split()
    z = int(zp[0])
    p = int(zp[1])
    cost[z] = p
    heappush(priority_queue, (p, z))

d = int(input())

while len(priority_queue) > 0:
    current_cost, city = heappop(priority_queue)
    if city == d:
        print(current_cost)
        break
    if city < len(graph):
        for i in range(1, len(graph[city])):
            new_cost = current_cost + graph[city][i]
            if new_cost < cost[i]:
                cost[i] = new_cost
                heappush(priority_queue, (new_cost, i))