n = int(input())

waves = input().split()
for i in range(n):
    waves[i] = int(waves[i])

min = min(waves)
max = max(waves)
min_idx = waves.index(min)
max_idx = waves.index(max)

if (max_idx <= min_idx):
    print('unknown')

else:
    for i in range(min_idx, max_idx):
        if (not(waves[i] < waves[i+1])):
            print('unknown')
            break

        if (i == max_idx-1):
            print(max-min)