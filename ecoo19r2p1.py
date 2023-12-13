for repeat in range(10):

    x = set()
    n = int(input())

    for i in range(n):

        next = input().lower()

        r = ''
        z = next.index('@')
        for i in range(z):
            if (next[i] == '+'):
                break
            if (next[i] == '.'):
                continue
            r += next[i]
        r += next[z:]

        x.add(r)

    print(len(x))