T = int(input())

for i in range(T):
    
    n = int(input())

    top = []
    branch = []
    for i in range(n):
        top.append(int(input()))

    count = 1
    while (len(top) > 0):
        if ((len(branch) > 0) and (branch[-1] == count)):
            branch.pop()
            count += 1
        else:
            if (top[-1] == count):
                top.pop()
                count += 1
            else:
                branch.append(top.pop())

    while (len(branch) > 0):
        if (branch[-1] == count):
            branch.pop()
            count += 1
        else:
            print('N')
            break

        if (len(branch) == 0):
            print('Y')