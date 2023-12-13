def get_next_distinct_year(y1, y2) -> int:

    for i in range(len(y2)):
        for j in range(len(y2)):
            if ((i != j) and (y2[i] == y2[j])):
                y1 = y1 +1
                y2 = str(y1)
                return get_next_distinct_year(y1, y2)
    return y2

y1 = int(input())+1
y2 = str(y1)

print(get_next_distinct_year(y1, y2))