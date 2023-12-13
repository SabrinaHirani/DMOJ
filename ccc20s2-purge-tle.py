import sys
from queue import Queue

input = sys.stdin.readline

m = int(input())
n = int(input())

graph = {}
for i in range(1, m + 1):
    values = [int(x) for x in input().split()]
    for j in range(len(values)):
        if values[j] not in graph:
            graph[values[j]] = set()
        graph[values[j]].add(i * (j + 1))

queue = Queue()
queue.put(m * n)
visited = set()
visited.add(m * n)

while not queue.empty():
    current = queue.get()
    if current in graph:
        for x in graph[current]:
            if x not in visited:
                visited.add(x)
                if x == 1:
                    break
                queue.put(x)

if 1 not in visited:
    print('no')
else:
    print('yes')