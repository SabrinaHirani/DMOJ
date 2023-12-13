menu = [[461, 431, 420, 0], [100, 57, 70, 0], [130, 160, 118, 0], [167, 266, 75, 0]]

c = 0

for i in range(4):
    c += menu[i][int(input())-1]

print('Your total Calorie count is ' + str(c) + '.')
