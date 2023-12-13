from bisect import bisect_left, bisect_right

nh = input().split()
n = int(nh[0])
h = int(nh[1])

stalagmite = []
stalactite = []
for i in range(n):
    if (i%2 == 0):
        stalagmite.append(int(input()))
    else:
        stalactite.append(int(input()))
stalagmite.sort()
stalactite.sort()

c = []
for i in range(1, h+1):
    x = len(stalagmite) - bisect_left(stalagmite, i)
    y = len(stalactite) - bisect_left(stalactite, h-(i-1))
    c.append(x+y)

x = min(c)
y = c.count(x)
print(x, y)