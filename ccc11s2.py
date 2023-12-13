n = int(input())

select = []
for i in range(n):
    select.append(input())

wrong = 0
for i in range(n):
    if (select[i] != input()):
        wrong += 1

print(n-wrong)