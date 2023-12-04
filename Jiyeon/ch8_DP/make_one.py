import sys

x = int(sys.stdin.readline())
dp = [0] * 30001 # 앞서 계산된 결과 저장 DP 테이블 초기화

for i in range(2, x+1):
    ## 1을 빼는 경우의 dp[i] 설정.
    dp[i] = dp[i-1] + 1 ## +1은, 해당 단계까지 가는 횟수 추가한 것

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # 2로 나누어질 때 가능한 계산의 경우는 '2로 나누는것' 또는 '1 빼는 것'. 이기 때문에 min 함수 사용
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[x])