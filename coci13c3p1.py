k = int(input())

a = 1
b = 0

for i in range(k):
    x = a
    a = b
    b = x+b

print(a, b)