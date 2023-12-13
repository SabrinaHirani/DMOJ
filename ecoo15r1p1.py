for repeat in range(10):

    color = ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']
    number = [0, 0, 0, 0, 0, 0, 0, 0]

    next = input()
    while (next != 'end of box'):
        number[color.index(next)] += 1

        next = input()

    t = 0
    for i in range(len(number)-1):
        t += number[i]//7
        if (number[i]%7 != 0):
            t += 1
        
    t *= 13
    t += (number[-1] * 16)

    print(t)