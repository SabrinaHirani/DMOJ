count = 0

C = int(input())
row1 = input().split()
row2 = input().split()

prev = False
for i in range(C):
    if not prev and row1[i] == '1':
        count += 3
        prev = True
    elif row1[i] == '1':
        count += 1
    else:
        prev = False

prev = False
for i in range(C):
    if not prev and row2[i] == '1':
        count += 3
        prev = True
    elif row2[i] == '1':
        count += 1
    else:
        prev = False

    if i%2 == 0 and row2[i] == '1' and row1[i] == '1':
        count -= 2

print(count)
