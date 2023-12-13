switch = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

n  = int(input())

m = {}
for i in range(n):
    next = input()

    x = ''
    for i in range(len(next)):
        x += str(switch[next[i]])

    if (m.get(x) == None):
        m[x] = 1
    else:
        m[x] += 1

print(m[input()])