for i in range(10):

    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])

    area = [[0,0], [1,-1]]

    idx = 1
    while not(area[0][0] <= x <= area[1][0] and area[1][1] <= y <= area[0][1]):
        n = 0
        idx += 1
        if idx == 2:
            n = 1
        else:
            n = max(abs(area[0][0] - area[1][0]), abs(area[0][1] - area[1][1]))

        if (idx-2)%4 == 0:
            area[0][0] -= n
        elif (idx-2)%4 == 1:
            area[0][1] += n 
        elif (idx-2)%4 == 2:
            area[1][0] += n
        else:
            area[1][1] -= n

    print(idx)