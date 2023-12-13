nm = input().split()
n = int(nm[0])
m = int(nm[1])

state = input().split()
toggle = input().split()

count = state.count('1')
for i in range(len(toggle)+1):

    if (count <= i):
        print(i)
        break

    if (i == len(toggle)):
        print(count)
        break

    toggle[i] = int(toggle[i])-1

    if (state[toggle[i]] != '1'):
        state[toggle[i]] = '1'
        count += 1
    else:
        state[toggle[i]] = '0'
        count -= 1