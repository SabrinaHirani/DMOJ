starting = input().split()
ending = input().split()

start = (int(starting[0]), int(starting[1]), 0)
stop = (int(ending[0]), int(ending[1]))

moves = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (2, -1), (-2, -1)]
queue = [start]
visited = set()

while len(queue) > 0:
    next = queue.pop(0)
    if (stop == (next[0], next[1])):
        print(next[2])
        break
    for i in range(len(moves)):
        x = next[0] + moves[i][0]
        y  = next[1] + moves[i][1]
        z = next[2]
        if 1 <= x <= 8 and 1 <= y <= 8:
            if (x,y) not in visited:
                queue.append((x,y, z+1))
                visited.add((x,y))