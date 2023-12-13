import math

a = int(input())
b = int(input())
c = int(math.ceil((a**(1/3))))
d = int(math.floor((b**(1/3))))

if (c > d):
    d = c+1

count = 0
for i in range(c, d+1):
    if (math.sqrt(i**3) == int(math.sqrt(i**3))):
        count += 1

print(count)