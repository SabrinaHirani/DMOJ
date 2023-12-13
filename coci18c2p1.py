game = {}

af = 0
bf = 0

a = int(input())
for i in range(a):
    x = int(input())
    game.update({x : True})
    if (i == 0):
        af = x


b = int(input())
for i in range(b):
    x = int(input())
    game.update({x : False})
    if (i == 0):
        bf = x

lead = (af > bf)

a = 0
b = 0
h = 0
t = 0

for k in sorted(game):
    if (k <= 1440):
        h += 1
    if (game[k]):
        a += 1
    else:
        b += 1
    if ((not(lead) and (a > b)) or ((lead) and (b > a))):
        t += 1
        lead = not(lead)

print(h)
print(t-1)