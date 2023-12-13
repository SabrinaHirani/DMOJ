from bisect import bisect_left

nm = input().split()
n = int(nm[0])
m = int(nm[1])

trees = input().split()

annotate = {}

maximum = 0
for i in range(n):
    trees[i] = int(trees[i])
    if (annotate.get(trees[i]) == None):
        annotate[trees[i]] = 0
    annotate[trees[i]] += 1

    if (trees[i] > maximum):
        maximum = trees[i]

height = []

count = 0
for i in range(maximum):
    count += annotate.get(i, 0)
    height.append(n-count)

height.reverse()
for i in range(len(height)-1):
    height[i+1] += height[i]

print(((len(height)-1) - bisect_left(height, m)))