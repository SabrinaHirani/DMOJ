import sys
input = sys.stdin.readline

nm = input().split()
n = int(nm[0])
m = int(nm[1])

graph = {}

for i in range(m):
    xy = input().split()
    if int(xy[0]) not in graph:
        graph[int(xy[0])] = []
    graph[int(xy[0])].append(int(xy[1]))

pq = input().split()
p = int(pq[0])
q = int(pq[1])

found = False

queue = [p]
visited = set()
visited.add(p)

while len(queue) > 0:
    next = queue.pop(0)
    if next == q:
        found = True
        print('yes')
        break
    if next in graph:
        for x in graph[next]:
            if x not in visited:
                queue.append(x)
                visited.add(x)

queue = [q]
visited = set()
visited.add(q)

while len(queue) > 0:
    next = queue.pop(0)
    if next == p:
        found = True
        print('no')
        break
    if next in graph:
        for x in graph[next]:
            if x not in visited:
                queue.append(x)
                visited.add(x)

if not found:
    print('unknown')