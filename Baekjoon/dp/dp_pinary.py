## 백준 dp 실버3 - 2193 이친수
import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)

dp[1] = 1

if n>=2:
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])