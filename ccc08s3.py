t = int(input())

for _ in range(t):
    r = int(input())
    c = int(input())

    grid = []

    for i in range(r):
        grid.append(input())

    queue = [(0, 0)]
    dist = [[float('inf') for _ in range(c)] for _ in range(r)]
    dist[0][0] = 1

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        next = queue.pop(0)
        x = grid[next[0]][next[1]]

        start, end = 0, 4
        if x == '*':
            start = 4
        elif x == '-':
            start = 2
        elif x == '|':
            end = 2

        for dir in move[start:end]:
            u = next[0] + dir[0]
            v = next[1] + dir[1]
            if 0 <= u < r and 0 <= v < c and grid[u][v] != '*' and dist[next[0]][next[1]] + 1 < dist[u][v]:
                dist[u][v] = dist[next[0]][next[1]] + 1
                queue.append((u,v))

    if dist[-1][-1] == float('inf'):
        print(-1)
    else:
        print(dist[-1][-1])
