import math

k = int(input()) +1

count = []

if (k <= (10**5)+1):
    count.append(k-1)

else:

    x = k

    while (x%2 == 0):
        count.append(1)
        x /= 2

    a = int(math.sqrt(x))+1
    for i in range(3, a, 2):

        while (x%i == 0):
            count.append(i-1)
            x /= i

        if (((a%2 == 0) and ((i == a-1) and (x > 2))) or (((a%2 == 1)) and (i == a-2) and (x > 2))):
            count.append(int(x)-1)

r = sum(count)

if ((r != 0) and (r <= 10**5)):
    print(r)
    for i in range(len(count)):
        print((str(i+1)+' ')*(count[i]), end='')
else:
    print('Sad Chris')