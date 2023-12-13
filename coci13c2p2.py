move = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
grid = []

rs = input().split()
r = int(rs[0])
s = int(rs[1])

emp = '*'*(s+2)
grid.append(emp)
for i in range(r):
    grid.append('*' + input() + '*')
grid.append(emp)

total = 0
maximum = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        count = 0
        if (grid[i][j] == '.'):
            for k in range(len(move)):
                if (grid[i+move[k][0]][j+move[k][1]] == 'o'):
                    count += 1
            if (count > maximum):
                maximum = count
        elif (grid[i][j] == 'o'):
            for k in range(len(move)):
                if (grid[i+move[k][0]][j+move[k][1]] == 'o'):
                    total += 1

total = total //2
total += maximum
print(total)