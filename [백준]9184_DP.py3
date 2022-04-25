# 재귀는 매번 계산을 반복하므로 시간이 오래걸림
# DP의 메모지에이션을 통해 시간 단축

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c] # 기록된 값 가져오기
    
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c) # 메모지에이션
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c- 1) - w(a - 1, b - 1, c - 1) #메모지에이션
    return dp[a][b][c]

while True:
    a, b, c=map(int, input().split())
    if a==-1 and b==-1 and c==-1: break
    else:
        print("w(%d, %d, %d) = %d" %(a,b,c,w(a,b,c)))


