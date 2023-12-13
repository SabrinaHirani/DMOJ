x = int(input())
n = int(input())

t = 0
for i in range(n):
    t += x
    t -= int(input())

print(t+x)