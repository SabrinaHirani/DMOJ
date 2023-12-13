n = int(input())
previous = 'left'

while (n != 99999):
    d1 = n//10000
    d2 = n//1000
    step = n%1000

    dir = ''
    if ((d1+d2) == 0):
        dir = previous
    elif ((d1+d2)%2 != 0):
        dir = "left"
    else:
        dir = "right"

    print(dir, step)

    n = int(input())
    previous = dir