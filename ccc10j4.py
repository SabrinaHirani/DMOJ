temperatures = input().split()[1:]

while len(temperatures) > 0:

    cycle = len(temperatures)-1

    r = 0
    change = []
    for i in range(1, len(temperatures)):

        change.append(int(temperatures[i])-int(temperatures[i-1]))

        if i-1 != 0 and change[r] == change[i-1]:
            if r == 0:
                cycle = i-1
            r += 1

        elif change[r] != change[i-1]:
            cycle = len(temperatures)-1
            r = 0

    print(cycle)

    temperatures = input().split()[1:]