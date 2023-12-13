nm = input().split()
n = int(nm[0])
m = int(nm[1])

x = set()
for i in range(n):
    x.add(input())

count = 0
for i in range(m):
    z = set()
    for j in range(int(input())):
        z.add(input())
    if (len(z.difference(x)) == 0):
        count += 1

print(count)