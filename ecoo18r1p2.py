for repeat in range(10):

    n = int(input())

    m = 70001
    routes = set()

    for i in range(n):
        route = input().split()
        id = int(route[0])
        k = int(route[1])

        for j in range(2, len(route)):
            x = int(route[j])
            if (x < m):
                routes.clear()
                m = x

            if (x == m):
                routes.add(id)

    print(m, '{', end='')
    for i in (sorted(routes)):
        if (i == sorted(routes)[-1]):
            print(str(i), end='')
        else:
            print(str(i)+',', end='')
    print('}')