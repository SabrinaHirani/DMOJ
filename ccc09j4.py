text = ['WELCOME', 'TO', 'CCC', 'GOOD', 'LUCK', 'TODAY']
length = [7, 2, 3, 4, 4, 5, 0]

w = int(input())
sign = []
 
x = 0
sum = 0
for i in range(len(length)-1):

    sum += length[i]

    if (w <= sum+length[i+1]):

        if (len(text[x:i+1]) == 1):
            sign.append(text[x:i+1][0] + '.'*(w-len(text[x:i+1][0])))
        else:
            r = 1+((w-sum)//(i-x))
            s = '.'*r
            next = s.join(text[x:i+1])
            next = next.replace(s, s+'.', w-sum-((r-1)*(i-x)))
            sign.append(next)

        sum = -1
        x = i+1

    if (length[i] == 5):
        if (x <= i):

            if (len(text[x:]) == 1):
                sign.append(text[x:][0] + '.'*(w-len(text[x:][0])))
            else:
                r = 1+((w-sum)//(len(text)-x))
                s = '.'*r
                next = s.join(text[x:])
                next = next.replace(s, s+'.', w-sum-((r-1)*(i-x)))
                sign.append(next)

    sum += 1

for i in range(len(sign)):
    print(sign[i])