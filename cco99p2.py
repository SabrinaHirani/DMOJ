switch = {'1': 'st', '2': 'nd', '3': 'rd'}

n = int(input())

for i in range(n):
    mk = input().split()
    m = int(mk[0])
    k = int(mk[1])

    suffix = str(k)
    if ((len(suffix) >= 2) and (suffix[-2:-1] == '1')):
        suffix = 'th'
    else:
        suffix = switch.get(suffix[-1:], 'th')

    x = {}
    for j in range(m):
        next = input()

        if next not in x:
            x[next] = 1
        else:
            x[next] += 1
       
    y = {}
    for next in x:
        if x[next] not in y:
            y[x[next]] = []
        y[x[next]].append(next)

    z = list(y.keys())
    z.sort(reverse=True)

    r = 1
    s = {}
    for j in range(len(z)):
        s[r] = z[j]
        r += len(y[z[j]])

    print('{0}{1} most common word(s):'.format(k, suffix))
    if (y.get(s.get(k)) != None):
        for j in y.get(s.get(k)):
            print(j)
    print()