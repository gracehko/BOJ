n = int(input())
sugar = [3, 5]
dp = [5001] * (n+1)

dp[0] = 0
for i in sugar:
    for j in range(1, n+1):
        if dp[j-i]!=5001:
            dp[j]=min(dp[j], dp[j-i]+1)

if dp[n]!=5001:
    print(dp[n])
else:
    print(-1)
