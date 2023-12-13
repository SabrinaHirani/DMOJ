constraint = [[1, 4], [1, 7], [2, 1], [3, 4], [3, 5]]
count = [-1, 0, -1, -1, 1, 0, -1, 0]

x = int(input())
y = int(input())

while ((x != 0) and (y != 0)):

    constraint.append([x, y])
    count[y] += 1

    x = int(input())
    y = int(input())

for i in range(1, 8):
    if (count[i] == -1):
        constraint.append([0, i])

constraint.sort()

order = []
values = set()

i = 0
while (i < len(constraint)):
    if (constraint[i][0] == 0):
        if (count[constraint[i][1]] > 0):
            count[constraint[i][1]] -= 1
            constraint.pop(i)
            i -= 1
        else:
            order.append(str(constraint[i][1]))
            for j in range(len(constraint)):
                if (constraint[i][1] == constraint[j][0]):
                    constraint[j][0] = 0
            constraint.pop(i)
            constraint.sort()
            i = -1
    i += 1

if (len(order) == 7):
    print(' '.join(order))
else:
    print('Cannot complete these tasks. Going to bed.')