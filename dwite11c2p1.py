for i in range(5):
    n = int(input())

    r = 0
    d = 0
    
    inc = 1
    sum = 1
    for step in range(n):
        if (sum == step):
            inc += 1
            sum += inc
        if (inc%2 == 1):
            r += 1
        else:
            d -= 1

    print(r, d)