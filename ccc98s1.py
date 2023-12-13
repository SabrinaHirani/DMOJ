n = int(input())

for i in range(n):
    x = input().split()
    for j in range(len(x)):
        if (len(x[j]) == 4):
            x[j] = '****'
    print(' '.join(x))