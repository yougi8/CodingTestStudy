## 백준 dp 실버3 - 1463 1로 만들기
import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(2, n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1]+1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0: ## 여기 elif 아님 주의!! if 여야함!!
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])