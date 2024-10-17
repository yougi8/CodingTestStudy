## 프로그래머스 등굣길 Lv3
def solution(m, n, puddles):
    board = [[0] * (m + 1) for _ in range(n + 1)]

    puddles = {(y, x) for x, y in puddles}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                board[i][j] = 1

            elif (i, j) in puddles:
                board[i][j] = 0

            else:
                board[i][j] = board[i - 1][j] + board[i][j - 1]

    return board[n][m] % 1000000007

## 문제 풀이
# 보통 n,m 이렇게 주어지는데 여기는 m,n 이렇게 주어진다.
# 그리고 주어지는 좌표가 (m,n) 이므로 앞의 변수가 가로위치이고 뒤의 변수가 세로 위치라는 것을 알아야 한다!
# 그리고 puddles를 set으로 바꿔서 검색이 더 빠르게 했다
# 뿐만 아니라 puddles를 set으로 바꾸는 과정에서 좌표로 치환해야 하기 때문에 (x,y)로 받는게 아니라 (y,x)로 받게 된다 <- 이 부분 때문에 계속 실패였음 ㅠ