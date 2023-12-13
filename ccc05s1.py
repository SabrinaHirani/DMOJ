switch = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5,'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

t = int(input())
for i in range(t):

    next = input()

    x = ''
    for j in range(len(next)):

        if ((next[j].isalpha()) or (next[j].isnumeric())):
            if (next[j].isalpha()):
                x += str(switch[next[j]])
            else:
                x += next[j]
             
            if (len(x) == 10):
                x = x[:3] + '-' + x[3:6] + '-' + x[6:]
                print(x)
                break