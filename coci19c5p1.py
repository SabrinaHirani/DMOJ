nm = input().split()
n = int(nm[0])
m = int(nm[1])

text = []
count = 0

text.append('.'*(m+1))
for i in range(n):
    text.append('.'+input())

for i in range(1, len(text)):
    for j in range(1, len(text[i])):
        if (text[i][j] == '*'):
            if ((text[i-1][j] != '*') and (text[i][j-1] != '*')):
                count += 1

print(count)