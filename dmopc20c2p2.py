nm = input().split()
n = int(nm[0])
m = int(nm[1])

scarf = input().split()
for i in range(n):
    scarf[i] = int(scarf[i])

left = {}
right = {}
for i in range(n):
    if (scarf[i] not in left):
        left[scarf[i]] = i
        right[scarf[i]] = i
    else:
        right[scarf[i]] = i

x = 0
for i in range(m):
    next = input().split()
    next[0] = int(next[0])
    next[1] = int(next[1])
    if (next[0] in left and next[1] in right):
        y = right[next[1]] - left[next[0]] + 1
        if (y > x):
            x = y
print(x)