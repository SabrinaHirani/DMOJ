n = int(input())

deck = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

x = 21
for i in range(n):
    c = int(input())
    deck[c] -= 1
    x -= c

l = 0
g = 0
for i in range(len(deck)):
    if (i <= x):
        l += deck[i]
    else:
        g += deck[i]

if (g >= l):
    print('DOSTA')
else:
    print('VUCI')