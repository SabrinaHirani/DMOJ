password = input()

if (not((len(password) >= 8) and (len(password) <= 12))):
    print('Invalid')
else:

    lower = 0
    upper = 0
    digit = 0
    illegal = False

    for i in range(len(password)):
        if (password[i].islower()):
            lower += 1
        elif (password[i].isupper()):
            upper += 1
        elif (password[i].isdigit()):
            digit += 1
        else:
            illegal = True
            break

    if (not((lower >= 3) and (upper >= 2) and (digit >= 1) and (not(illegal)))):
        print('Invalid')
    else:
        print('Valid')