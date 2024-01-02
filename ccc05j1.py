daytime = int(input())
evening = int(input())
weekend = int(input())

A = max((daytime-100)* 0.25, 0) + evening*0.15 + weekend*0.20
B = max((daytime-250)* 0.45, 0) + evening*0.35 + weekend*0.25

A = round(A, 2)
B = round(B, 2)

print('Plan A costs %.2f' % A)
print('Plan B costs %.2f' % B)

if A == B:
    print('Plan A and B are the same price.')
elif A < B:
    print('Plan A is cheapest.')
else:
    print('Plan B is cheapest.')
