adr = ['A', 'B', 'C']
bru = ['B', 'A', 'B', 'C']
gor = ['C', 'C', 'A', 'A', 'B', 'B']

n = int(input())
answer = input()

a = 0
b = 0
g = 0

for i in range(n):

    if (answer[i] == adr[i%len(adr)]):
        a += 1

    if (answer[i] == bru[i%len(bru)]):
        b += 1
    
    if (answer[i] == gor[i%len(gor)]):
        g += 1

m = max(a, b, g)
print(m)

if (a == m):
    print('Adrian')
if (b == m):
    print('Bruno')
if (g == m):
    print('Goran')