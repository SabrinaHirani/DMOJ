switch = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
alphabet = '1bcd2fgh3jklmn4pqrst5vwxyz'
word = input()

rov = ''
for i in range(len(word)):
    if (word[i] in 'aeiou'):
        rov += word[i]
    else:
        rov += word[i]
        x = alphabet.index(word[i])

        j = 1
        while((not(alphabet[max(0, x-j)].isnumeric())) and (not(alphabet[min(x+j, 25)].isnumeric()))):
            j += 1
        if (alphabet[max(0, x-j)].isnumeric()):
             j *= -1
        rov += switch[alphabet[x+j]]

        k = 1
        while (alphabet[min(x+k, 25)].isnumeric()):
            k += 1
        rov += alphabet[min(x+k, 25)]

print(rov)