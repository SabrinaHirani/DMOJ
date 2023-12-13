def count_room(i, j, r, c, grid, visited):
    count = 0
    queue = [(i, j)]
    visited.add((i,j))
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while len(queue) > 0:
        i, j = queue.pop(0)
        count += 1
        for dir in move:
            u = i + dir[0]
            v = j + dir[1]
            if 0 <= u < r and 0 <= v < c and grid[u][v] != 'I' and (u, v) not in visited:
                queue.append((u, v))
                visited.add((u, v))

    return count

n = int(input())
r = int(input())
c = int(input())

grid = []
visited = set()

for i in range(r):
    grid.append(input())

rooms = []

for i in range(r):
    for j in range(c):
        if grid[i][j] != 'I' and (i,j) not in visited:
            rooms.append(count_room(i, j, r, c, grid, visited))

rooms.sort(reverse=True)

count = 0
while len(rooms) > 0 and n-rooms[0] >= 0:
    n -= rooms.pop(0)
    count += 1

if count == 1:
    print(f"{count} room, {n} square metre(s) left over")
else:
    print(f"{count} rooms, {n} square metre(s) left over")
