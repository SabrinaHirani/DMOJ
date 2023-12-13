nh = input().split()
n = int(nh[0])
h = int(nh[1])

c_health = h
d_health = h

action = []
damage = []

for i in range(n):
    next = input().split(' ')
    action.append(next[0])
    if (next[0] == 'A'):
        damage.append(int(next[1]))
    elif (next[0] == 'D'):
        damage.append(int(next[1])*(-1))


for i in range(1, 2*n+1, 2):
    next = input().split(' ')
    action.insert(i, next[0])
    if (next[0] == 'A'):
        damage.insert(i, int(next[1]))
    elif (next[0] == 'D'):
        damage.insert(i, int(int(next[1]))*(-1))

for i in range(n*2):

    if (i%2 == 0):

        if (action[i] == 'A' and (i == 0 or action[i-1] != 'D')):
            d_health -= damage[i]
        elif (action[i] == 'D' and (i == 2*n-1 or action[i+1] != 'A')):
            c_health += damage[i]

    else:

        if (action[i] == 'A' and (i == 0 or action[i-1] != 'D')):
            c_health -= damage[i]
        elif (action[i] == 'D' and (i == 2*n-1 or action[i+1] != 'A')):
            d_health += damage[i]

    if (d_health <= 0 and c_health <= 0):
        print('TIE')
        break
    elif (c_health <= 0):
        print('DEFEAT')
        break
    elif (d_health <= 0):
        print('VICTORY')
        break

    if (i == n*2-1):
        print('TIE')