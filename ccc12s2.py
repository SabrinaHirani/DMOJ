a = input()

roman = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

m = 0
count = 0
for i in range(len(a)-1, 0, -2):
    x = roman[a[i]]
    if (m <= x):
        count += int(a[i-1])*x
    else:
        count -= int(a[i-1])*x
    m = x

print(count)