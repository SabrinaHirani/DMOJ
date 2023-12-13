n = int(input())
length = input().split()
store = [0 for x in range(2001)]
count = [0 for x in range(4001)]

for i in range(len(length)):
    store[int(length[i])] += 1

max = 0
for i in range(len(store)):
    for j in range(i, len(store)):
        if (i == j):
             count[i+j] += store[i]//2
        else:
            count[i+j] += min(store[i], store[j])

        if (count[i+j] > max):
            max = count[i+j]

print(max, count.count(max))