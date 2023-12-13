import sys
input = sys.stdin.readline

tnmg = input().split()
t = int(tnmg[0])
n = int(tnmg[1])
m = int(tnmg[2])
g = int(tnmg[3])

food_basics = set()
for i in range(g):
    food_basics.add(int(input()))

graph = {}
for i in range(m):
    abl = input().split()
    a = int(abl[0])
    b = int(abl[1])
    l = int(abl[2])
    if a not in graph:
        graph[a] = []
    graph[a].append((b, l))

queue = [(0,0)]
visited = set()
visited.add(0)

count = 0
while len(queue) > 0:
    building, distance = queue.pop(0)
    if building in food_basics:
        count += 1
    if building in graph:
        for b,l in graph[building]:
            if b not in visited and distance+l <= t:
                queue.append((b,distance+l))
                visited.add(b)

print(count)