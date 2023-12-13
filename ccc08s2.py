import math

next = int(input())
while (next != 0):

    count = 0
    for i in range(next):
        count += int(math.sqrt(next**2 - i**2))
    print((4*count)+1)

    next = int(input())