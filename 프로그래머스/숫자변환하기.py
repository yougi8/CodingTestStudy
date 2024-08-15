## 프로그래머스 - 숫자 변환하기 https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    INF = 1e9
    dp = [INF] * (y + 1)

    # 출발점인 x에서는 더한 값이 0
    dp[x] = 0

    for i in range(x, y + 1):
        # 시간복잡도 개선으로 추가된 코드
        # : 출발지점인 dp[x]는 0으로 초기화되어있고, 순차적으로 살펴보니까 만약 현재 살펴보고 있는 dp[i]가 INF값이라면 주어진 연산으로는 만들 수 없는 값이다. 그래서 아래 3가지 비교연산 패스
        if dp[i] == INF:
            continue

        # dp[i]+1이랑 비교하는 이유 : dp[i+n], dp[i*2], dp[i*3]은 각각 i번째에서 n을 더하거나 2를 곱하거나 3을 곱하는 연산 1회 수행해서 도착할 수 있기 때문
        if i + n <= y:
            dp[i + n] = min(dp[i] + 1, dp[i + n])
        if i * 2 <= y:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])
        if i * 3 <= y:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])

    if dp[y] == INF:
        return -1
    else:
        return dp[y]

solution(10,40,5)
solution(10,40,30)
solution(2,5,4)

## 문제 풀이
# dp에서 min값 비교하는 대상 찾는 게 좀 생각하기 쉽지 않았음!
# dp[i]+1이랑 비교하는 건 알겠는데, 그 비교대상이 무엇인지가 애매했는데
# 같은 30이라도 10에서 5를 4번 더해서 오는 것과 10에서 3을 한번 곱해서 오는 두가지 경우가 있을 수 있는데
# 이때 더 작은 값을 업데이트 쳐줘야 하니까, 자기 자신과 비교하는 것이 필요하다고 판단했다!
# dp는 역시 어렵다...