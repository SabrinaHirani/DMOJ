import sys
input = sys.stdin.readline

for repeat in range(10):

    n = int(input())
    keys = set(map(int, input().split()))
    maximum = max(keys)

    count = 0
    for k in keys:
        x = k*2
        while (x <= maximum):
            if (x in keys):
                count += 1
            x += k

    print(count)