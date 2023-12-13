def sort_by_length(e):
    return len(e[0])

s = input()

combo = []
m = int(input())
for i in range(m):
    combo.append(input().split())

combo.sort(key=sort_by_length, reverse=True)

score = 0

i = 0
while (i < len(s)):
    for j in range(len(combo)):
        if (combo[j][0] == s[i:i+len(combo[j][0])]):
            score += int(combo[j][1])
            i += len(combo[j][0])-1
            break
    i += 1

print(score+len(s))