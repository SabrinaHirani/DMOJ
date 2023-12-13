p = int(input())
n = int(input())
r = int(input())

d = 0
change = n
while (p >= n):
    x = n
    n += (change*r)
    change = n-x
    d += 1

print(d)