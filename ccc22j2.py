n = int(input())

count = 0
for i in range(n):

    a = int(input())*5
    b = int(input())*3

    if ((a-b) > 40):
        count += 1

print(count, end='')
if (count == n):
    print('+')