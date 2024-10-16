## 프로그래머스 Lv2. 가장 큰 정사각형 찾기
def solution(board):
    answer = 0

    n = len(board)
    m = len(board[0])

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    for i in board:
        answer = max(answer, max(i))
    return answer ** 2