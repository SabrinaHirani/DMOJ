n = int(input())
system = input()

count = 0
last = '0'
for i in range(n-1, -1, -1):
    if (system[i] != last):
        last = system[i]
        count += 1

print(count)