# 2와 1의 조합으로 n을 만들 수 있는 방법
dp = [0] * 1001
dp[1]=1
dp[2]=2
for i in range(3, 1001):
    dp[i]=dp[i-1]+dp[i-2]

n = int(input())
print(dp[n]%10007)
