n = int(input())

s = 0
t = 0

for i in range(n):
    text = input()
    s += text.lower().count('s')
    t += text.lower().count('t')

if (s == t):
    print('French')
elif (s < t):
    print('English')
else:
    print('French')