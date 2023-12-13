start = [9, 40, 54, 67, 90, 99]
end = [34, 64, 19, 86, 48, 77]

x = 1
next = -1

while (True):

    next = int(input())
    if (x+next <= 100):
        x += next

    if (next == 0):
        print('You Quit!')
        break

    if (x in start):
        x = end[start.index(x)]

    print("You are now on square", x)

    if (x == 100):
        print('You Win!')
        break