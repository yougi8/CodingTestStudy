## 백준 실버3 퇴사 https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline

n = int(input())
info = [] # (기간,비용)
for i in range(n):
    info.append(list(map(int, input().split())))

dp = [0]*(n+1)

for i in range(n):
    # i번째 날까지의 최대 수익을 다음 날로 전달해줌
    if i + 1 <= n:
        dp[i+1] = max(dp[i+1], dp[i])

    # 상담이 기간 내에 끝나서 진행할 수 있다면
    if i + info[i][0] <= n:
        dp[i+info[i][0]] = max(dp[i+info[i][0]], dp[i] + info[i][1]) # 상담 끝난 시점의 dp값 갱신
print(max(dp))

## input
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
## output
# 45