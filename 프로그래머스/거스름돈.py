## 프로그래머스 Lv3 거스름돈 - https://school.programmers.co.kr/learn/courses/30/lessons/12907
def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for coin in money:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
    return dp[n]%1000000007

## 문제 풀이
# dp!