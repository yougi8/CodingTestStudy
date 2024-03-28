## 기출문제 ch.16 dp - q31 금광
import sys
t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split()) # n x m (n은 세로로 증가, m은 가로로 증가)
    array = list(map(int, sys.stdin.readline().split())) # 왼쪽에서 오른쪽으로, 위에서 아래로 순서

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index+m])
        index += m

    ## 첫번째 열은 왼쪽에서 오는 경우가 없기 때문에, 건너뛰고 시작한다. (index 1부터 시작)
    for i in range(1, m): # i는 몇 번째 열인지 나타내는 변수 ( 그래서 m만큼 반복 )
        for j in range(n): # j는 몇 번째 행인지 나타내는 변수 (그래서 n만큼 반복)
            ## 왼쪽 위에서 오는 경우
            if j-1 >= 0: # dp 범위 벗어나는지 체크 ( 왼쪽에 값이 있다는 것은 확실하니, 위아래로만 따진다 )
                left_up = dp[j-1][i-1] # (행,열) 이기 때문에 j를 먼저 쓴다.
            else:
                left_up = 0

            ## 왼쪽에서 오는 경우
            left = dp[j][i-1]

            ## 왼쪽 아래에서 오는 경우
            if j+1 < n: # dp 범위 벗어나는지 체크 ( 왼쪽에 값이 있다는 것은 확실하니, 위아래로만 따진다)
                left_down = dp[j+1][i-1]
            else:
                left_down = 0
            dp[j][i] = dp[j][i] + max(left_up, left, left_down)

    ## 최대값은, 마지막열에서 가장 큰 값이 된다
    result = 0
    for i in range(n):
        if dp[i][m-1] > result:
            result = dp[i][m-1]

    print(result)

### 생각 정리
# - for문 안에서 i, j가 몹시 헷갈렸다. 어떤 것이 n 좌표이고, m 좌표인지 바로바로 인식이 안된다.

