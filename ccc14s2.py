n = int(input())

n1 = input().split()
n2 = input().split()

partner = {}

for i in range(len(n1)):
    if (n1[i] == n2[i]):
        print('bad')
        break

    if (((partner.get(n1[i]) != None) and (partner[n1[i]] != n2[i])) or ((partner.get(n2[i]) != None) and (partner[n2[i]] != n1[i]))):
        print('bad')
        break

    partner[n1[i]] = n2[i]

    if (i == len(n1)-1):
        print('good')