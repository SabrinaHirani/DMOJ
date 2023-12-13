elder = input()
elders = [elder]

n = int(input())

for i in range(n):
    z1, z2 = input().split(' ')
    if (elder == z2):
        elder = z1
        if (not(elders.count(z1) > 0)):
            elders.append(z1)

print(elder)
print(len(elders))