book = {}
ending = []

N = int(input())
for i in range(1, N+1):
    book[i] = input().split()[1:]
    if len(book[i]) == 0:
        ending.append(i)

queue = [1]
visited = set()

visited.add(1)
dist = {1:1}

while len(queue) > 0:
    next = queue.pop(0)
    for x in book[next]:
        x = int(x)
        if x not in visited:
            queue.append(x)
            visited.add(x)
            dist[x] = dist[next]+1

shortest = float('inf')
for x in ending:
    if x in visited and dist[x] < shortest:
            shortest = dist[x]

if len(visited) != N:
     print("N")
else:
    print("Y")
print(shortest)