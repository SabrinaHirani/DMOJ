nq = input().split()
n = int(nq[0])
q = int(nq[1])

strokes = []
for i in range(q):
    next = input().split()
    strokes.append([int(next[0]), int(next[1])])
strokes.sort()

blue = 0
right = 0
for i in range(len(strokes)):
    if (strokes[i][0] <= right):
        if (strokes[i][1] > right):
            blue += strokes[i][1] - right
            right = strokes[i][1]
    else:
        blue += strokes[i][1] - strokes[i][0]
        right = strokes[i][1]
print(n-blue, blue)