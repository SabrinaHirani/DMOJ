n = int(input())

students = []

for i in range(n):
    students.append(set())

    next = input().split()
    students[i].add(int(next[0]))
    students[i].add(int(next[1]))

count = 0
maximum = [0, 0, 0, 0, 0]
for i in range(5):
    for j in range(len(students)):
        if (i+1 in students[j]):
            count += 1
        elif (count != 0):
            if (count > maximum[i]):
                maximum[i] = count
            count = 0
        
        if (j == len(students)-1):
            if (count > maximum[i]):
                maximum[i] = count
            count = 0

x = max(maximum)
z = maximum.index(x)+1
print(x, z)