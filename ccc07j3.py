sc = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())

for i in range(n):
    sc[int(input())] = 0

sc.pop(0)
a = (sum(sc))/(10-n)
b = int(input())

if (b > a):
    print('deal')
else:
    print('no deal')