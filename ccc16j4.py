time = input().split(":")
h = int(time[0])
m = int(time[1])

commute_time = 120
time_taken = 0

while commute_time > 0:
    x = 0
    if 7 <= h < 10 or 15 <= h < 19:
        x = min((60-m)//2, commute_time)
        m += x*2
    else:
        x = min(60-m, commute_time)
        m += x
    commute_time -= x
    if m >= 60:
        h += m//60
        m = m%60
        h = h%24

arrival_time = "{:02d}:{:02d}".format(h, m)
print(arrival_time)
