for repeat in range(10):

    fd = input().split()
    f = int(fd[0])
    d = int(fd[1])

    bakery = []
    bonus = 0

    for i in range(d):

        sum = 0
        temp = input().split()

        for j in range(f):
            temp[j] = int(temp[j])
            sum += temp[j]

        if (sum%13 == 0):
            bonus += sum/13

        bakery.append(temp)


    for i in range(f):

        sum = 0

        for j in range(d):

            sum += bakery[j][i]

        if (sum%13 == 0):
            bonus += sum/13

    print(int(bonus))