t1 = int(input())
t2 = int(input())
x = t1-t2

count = 2
while (x >= 0):
    count += 1
    t1 = t2
    t2 = x
    x = t1-t2

print(count)