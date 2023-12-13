q = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

count = 0
while q >= 1:

    q -= 1

    if (count%3 == 0):

        m1 += 1

        if (m1%35 == 0):
            q += 30

    elif (count%3 == 1):

        m2 += 1

        if (m2%100 == 0):
            q += 60

    elif (count%3 == 2):

        m3 += 1

        if (m3%10 == 0):
            q += 9

    count += 1

print('Martha plays', count, 'times before going broke.')