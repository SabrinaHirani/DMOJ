switch = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for repeat in range(5):

    next = input()
    next = next[next.index('TATAAT')+10:]

    tnext = ''
    for i in range(len(next)):
        tnext += switch.get(next[i])

    for i in range(6, len(next)//2):
        for j in range(len(next)-i+1):
            target = next[j:j+i][::-1]
            if (tnext[j+i:].find(target) != -1):
                tnext = tnext[:j]
                break

    tnext = tnext.replace('T', 'U')

    print(str(repeat+1) + ':', tnext)