text = input()

count = 0
target = 0

block = ['h', 'o', 'n', 'i']

for i in range(len(text)):
    if (text[i].lower() == block[target]):
        if (target != 3):
            target += 1
        else:
            target = 0
            count += 1

print(count)