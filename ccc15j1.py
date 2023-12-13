MONTH, DAY = 2, 18

m = int(input())
d = int(input())

if m < MONTH:
    print('Before')
elif m > MONTH:
    print('After')
else:
    if d < DAY:
        print('Before')
    elif d > DAY:
        print('After')
    else: 
        print('Special')