rs = input().split()
r = int(rs[0])
s = int(rs[1])

grid = []
start = []
stop = '.o*'

grid.append('*'*(s+2))
for i in range(r):
    grid.append('*' + input() + '*')
    if ('o' in grid[i]):
        start = [i, grid[i].index('o')]
grid.append('*'*(s+2))

path = []
dir1 = [[-1, 0], [1, 0], [0, 1], [0, -1]]
dir2 = ['N', 'S', 'E', 'W']

for i in range(4):
    dist = 0
    r = dir1.pop(0)
    s = [start[0] + r[0], start[1] + r[1]]
    while (grid[s[0]][s[1]] not in stop):
        if (grid[s[0]][s[1]] == 'x'):
            path.append((dir2[i], dist))
            break
        else:
            dist += 1
            if (grid[s[0]][s[1]] == '^'):
                s[0] -= 1
            elif (grid[s[0]][s[1]] == 'v'):
                s[0] += 1
            elif (grid[s[0]][s[1]] == '>'):
                s[1] += 1
            elif (grid[s[0]][s[1]] == '<'):
                s[1] -= 1

path.sort(key=lambda x:x[0])
path.sort(key=lambda x:x[1])
if (len(path) > 0):
    print(':)')
    print(path[0][0])
else:
    print(':(')