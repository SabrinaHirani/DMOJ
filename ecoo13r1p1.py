n = int(input())

count = 0
uncount = 0

next = input()
while (next != 'EOF'):

    if (next == 'TAKE'):
        n += 1
        if (n > 999):
            n -= 999
        count += 1

    elif (next == 'SERVE'):
        uncount += 1

    else:
        print(count, (count-uncount), n)
        count = 0
        uncount = 0
    
    next = input()