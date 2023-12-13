n = int(input())

m = []
for i in range(n):
    m.append(int(input()))

next = int(input())
while (next != 77):

    if (next == 99):

        idx = int(input())
        m.insert(idx, m[idx-1])

        ratio = int(input())
        m[idx-1] = m[idx-1]*(ratio/100)
        m[idx] = m[idx]*((100-ratio)/100)

    else:

        idx = int(input())
        m[idx-1] += m[idx]
        m.pop(idx)
    
    next = int(input())

for i in range(len(m)):
    print(round(m[i]), end=' ')