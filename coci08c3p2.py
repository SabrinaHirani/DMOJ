text = input()
res = ''

i = 0
while (i < len(text)):
    res += text[i]
    if (text[i] in 'aeiou'):
        i+=2
    i += 1

print(res)