song = input()

main_a = 0
main_c = 0

next = True
for i in range(len(song)):
    if (next):
        if ((song[i] == 'A') or (song[i] == 'D') or (song[i] == 'E')):
            main_a += 1
        elif ((song[i] == 'C') or (song[i] == 'F') or (song[i] == 'G')):
            main_c += 1
        next = False
    elif (song[i] == '|'):
        next = True

if (main_a == main_c):
    if ((song[len(song)-1] == 'A') or (song[len(song)-1] == 'D') or (song[len(song)-1] == 'E')):
        print("A-mol")
    elif ((song[len(song)-1] == 'C') or (song[len(song)-1] == 'F') or (song[len(song)-1] == 'G')):
        print("C-dur")
elif (main_a > main_c):
    print("A-mol")
else:
    print("C-dur")