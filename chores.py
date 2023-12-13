n = int(input())

chores = []
for i in range(n):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    chores.append((a,b))

chores.sort(key=lambda x: x[0])

score = 0
time = 0
for i in range(n):
    a, b = chores[i]
    score += (time*b) + (a*(b*(b+1))//2)
    time += a*b

print(score%(10**9+7))