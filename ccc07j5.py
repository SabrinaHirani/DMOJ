a = int(input())
b = int(input())
n = int(input())

motel = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

for i in range(n):
    motel.append(int(input()))
motel.sort()

options = [0]*len(motel)
options[0] = 1

for i in range(1, len(motel)):
    j = i-1
    while j >= 0:
        distance = motel[i]-motel[j]
        if a <= distance and distance <= b:
            options[i] += options[j]
        elif distance > b:
            break
        j -= 1

print(options[-1])