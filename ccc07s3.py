import sys
input = sys.stdin.readline

n = int(input())

graph = {}

for i in range(n):
    xy = input().split()
    graph[int(xy[0])] = int(xy[1])

pq = input().split()
p = int(pq[0])
q = int(pq[1])

while not(p == 0 and q == 0):

    queue = [(p, -1)]
    visited = set()
    visited.add(p)

    found = False
    seperation = 0
    while len(queue) > 0:
        next, count = queue.pop(0)
        if next == q:
            found = True
            seperation = count
        if found and graph[next] in visited:
            print('Yes', seperation)
            break
        elif graph[next] != None and graph[next] not in visited:
            queue.append((graph[next], count+1))
            visited.add(graph[next])

    if not found:
        print('No')
    
    pq = input().split()
    p = int(pq[0])
    q = int(pq[1])

