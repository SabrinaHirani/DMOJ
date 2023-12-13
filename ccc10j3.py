var = {"A":0, "B":0, "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

instruction = input()
while (instruction != '7'):

    if (instruction[0] == '1'):
        var[instruction[2]] = int(instruction[4:])
    elif (instruction[0] == '2'):
        print(var[instruction[2]])
    elif (instruction[0] == '3'):
        var[instruction[2]] += var[instruction[4]]
    elif (instruction[0] == '4'):
        var[instruction[2]] *= var[instruction[4]]
    elif (instruction[0] == '5'):
        var[instruction[2]] -= var[instruction[4]]
    else:
        var[instruction[2]] = var[instruction[2]] // var[instruction[4]]

    instruction = input()