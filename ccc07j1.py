w1 = int(input())
w2 = int(input())
w3 = int(input())

if w1-w2 > 0:
    if w1-w3 > 0:
        if w2-w3 > 0:
            print(w2)
        else:
            print(w3)
    else:
        print(w1)
else:
    if w2-w3 > 0:
        if w1-w3 > 0:
            print(w1)
        else:
            print(w3)
    else:
        print(w2)