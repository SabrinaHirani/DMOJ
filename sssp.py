nm = input().split()
n = int(nm[0])
m = int(nm[1])

graph = {}
weight = {}

for i in range(m):
    uvw = input().split()
    u = int(uvw[0])
    v = int(uvw[1])
    w = int(uvw[2])
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    graph[u].add(v)
    graph[v].add(u)
    if (u,v) not in weight or w < weight[(u,v)]:
        weight[(u,v)] = w
        weight[(v,u)] = w

queue = [1]
dist = {1:0}

while len(queue) > 0:
    next = queue.pop(0)
    for x in graph[next]:
        if x not in dist or dist[next]+weight[(next,x)] < dist[x]:
            dist[x] = dist[next]+weight[(next,x)]
            queue.append(x)

for i in range(1, n+1):
    if i in dist:
        print(dist[i])
    else:
        print(-1)