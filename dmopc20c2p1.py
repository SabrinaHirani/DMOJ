n = int(input())
change = input()

money = 1
worth = []
sign = []

for i in range(n):

    if (change[i] == '^'):
        sign.append('/')

        worth.append(money)
        money += 1

    elif (change[i] == 'v'):
        sign.append('\\')

        money -= 1
        worth.append(money)

    elif (change[i] == '>'):

        sign.append('_')
        worth.append(money)

min = min(worth)
max = max(worth)
adj = 0
if (min <= 0):
    adj = abs(min)+1

for i in range(max+adj, 0, -1):
    for j in range(len(worth)):
        if (worth[j] == i-adj):
            print(sign[j], end='')
        else:
            print('.', end='')
    print('\n', end='')