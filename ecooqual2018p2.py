T = int(input())

for i in range(T):
    next = input()
    z = next.index('C')
    x = 'Educational '*(z)
    x += 'Computing '
    x += 'Organization of Ontario '*(((len(next)-(z+1))//2))
    print(x)