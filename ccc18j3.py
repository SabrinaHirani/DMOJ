def dist_from_next_city(x, dist):
    res = ''
    for i in range(5):
        if (i == x):
            res += '0' + ' '
        elif (i < x):
            res += str(str((sum(dist[i+1:x+1]))) + str(' '))
        else:
            res += str(str((sum(dist[x+1:i+1]))) + str(' '))
    return res



dist = [0]
dist.extend(input().split())
for i in range(1, len(dist)):
    dist[i] = int(dist[i])

for x in range(5):
    print(dist_from_next_city(x, dist))