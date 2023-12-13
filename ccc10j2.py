a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky = 0
bryon = 0

for i in range(s):
    if (i < a):
        nikky += 1
    elif (i < a+b):
        nikky -= 1
    elif (i < a+a+b):
        nikky += 1
    elif (i < 2*(a+b)):
        nikky -= 1
    else:
        nikky += 0

    if (i < c):
        bryon += 1
    elif (i < c+d):
        bryon -= 1
    elif (i < (2*c)+d):
        bryon += 1
    elif (i < 2*(c+d)):
        bryon -= 1
    else:
        bryon += 0

    if ((i > (2*(a+b))) and (i > (2*(c+d)))):
        break

if (nikky == bryon):
    print('Tied')
elif (nikky > bryon):
    print('Nikky')
else:
    print('Byron')