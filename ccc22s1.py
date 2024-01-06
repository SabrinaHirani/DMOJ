n = int(input())

dp = [0]*(max(5+1, n+1))
dp[0] = 1
dp[4] = 1
dp[5] = 1

for i in range(6, n+1):
        if (i < 9):
            dp[i] = dp[i-4] + dp[i-5]
        else:
            dp[i] = dp[i-4] + dp[i-5] - dp[i-9]

print(dp[n])
