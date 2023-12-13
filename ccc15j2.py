h = 0
s = 0

text = input()
h += text.count(':-)')
s += text.count(':-(')

if h == 0 and s == 0:
    print('none')
elif h == s:
    print('unsure')
elif h > s:
    print('happy')
else:
    print('sad')