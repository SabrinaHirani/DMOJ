import sys
input = sys.stdin.readline

def factor(x, m, n):
    z = []
    for i in range(1, int(x**(0.5))+1):
        if x%i == 0:
            if i <= m and x//i <= n:
                z.append((i, x//i))
            if x//i <= m and i <= n:
                z.append((x//i, i))
    return z

m = int(input())
n = int(input())

grid = [[0] for _ in range(m+1)]
for i in range(1, m+1):
     grid[i].extend([int(x) for x in input().split()])

queue = [(1,1)]
visited = set()
visited.add((1,1))

while len(queue) > 0:
    i, j = queue.pop(0)
    for x in factor(grid[i][j], m, n):
         if x not in visited:
             visited.add(x)
             if (m,n) in visited:
                 break
             queue.append(x)

if (m,n) not in visited:
     print('no')
else:
     print('yes')