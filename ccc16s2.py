p = int(input())
n = int(input())

dmoj = input().split()
peg = input().split()

for i in range(n):
    dmoj[i] = int(dmoj[i])
    peg[i] = int(peg[i])

if (p == 1):

    dmoj.sort()
    peg.sort()

else:

    dmoj.sort()
    peg.sort(reverse=True)

count = 0
for i in range(n):
    count += max(dmoj[i], peg[i])

print(count)