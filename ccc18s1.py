n = int(input())

street = []
for i in range(n):
    street.append(int(input()))
street.sort()

s = ((street[1] - street[0])/2) + ((street[2] - street[1])/2)
m = s

for i in range(2, n-1):
    s = ((street[i] - street[i-1])/2) + ((street[i+1] - street[i])/2)
    if (s < m):
        m = s

print(m)