import sys
input = sys.stdin.readline

n = int(input())

freq = {}
inv_freq = {}

for i in range(n):
    r = int(input())

    if (not(r in freq)):
        freq[r] = 0
    freq[r] += 1

    if (not(freq[r] in inv_freq)):
        inv_freq[freq[r]] = set()
    inv_freq[freq[r]].add(r)

    if (freq[r] > 1):
        inv_freq[freq[r]-1].remove(r)
        if (len(inv_freq[freq[r]-1]) == 0):
            inv_freq.pop(freq[r]-1)

readings = set(inv_freq.keys())
x = max(readings)

if (len(inv_freq[x]) < 2):
    readings.remove(x)
    y = max(readings)

    v = min(inv_freq[y])
    u = max(inv_freq[y])
    print(max(abs(list(inv_freq[x])[0]-v), abs(list(inv_freq[x])[0]-u)))
else:
    v = min(inv_freq[x])
    u = max(inv_freq[x])
    print(u-v)