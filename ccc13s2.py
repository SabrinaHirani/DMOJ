w = int(input())
n = int(input())

c = []

for i in range(n):
    c.append(int(input()))

for i in range(n):
    if (i < 3):
        if (i == 0 and (w-c[0] < 0)):
            print(i)
            break
        elif (i == 1 and (w-(c[0] + c[1]) < 0)):
            print(i)
            break
        elif (i == 2 and (w-(c[0] + c[1] + c[2]) < 0)):
            print(i)
            break
    else: 
        if (w-(c[i] + c[i-1] + c[i-2] + c[i-3]) < 0):
            print(i)
            break
        if (i == (n-1)):
            print(n)