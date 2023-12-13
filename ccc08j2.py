b = 0
n = 0

playlist = 'ABCDE'

while (not((b == 4) and (n == 1))):

    b = int(input())
    n = int(input())

    if (b == 1):

        for i in range(n%len(playlist)):
            playlist = playlist[1:] + playlist[0]

    elif (b == 2):

        for i in range(n%len(playlist)):
            playlist = playlist[-1] + playlist[:len(playlist)-1]

    elif (b == 3):

        if (n%2 == 1):
            playlist = playlist[1] + playlist[0] + playlist[2:]

    else:

        for i in playlist:
            print(i, '', end='')