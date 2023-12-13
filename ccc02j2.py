text = input()

while (text != 'quit!'):

    if ((len(text) > 4) and (text[-2:] == 'or') and (not(text[-3] in 'aeiouy'))):
        print(text[:-2] + 'our')
    else:
        print(text)

    text = input()