# ## 프로그래머스 - 169199 리코쳇 로봇
from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    start = [0, 0]
    goal = [0, 0]

    ## step1. 시작 지점 기록
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = [i, j]
                break

    ## step2. bfs로 미끄러지기
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[start[0]][start[1]] = True

    while q:
        x, y, value = q.popleft()

        if board[x][y] == 'G':
            return value

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 장애물을 마주치기 전까지 한 방향으로 미끄러지기
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                nx += dx[i]
                ny += dy[i]

            # 장애물/보드 끝에 닿아서 while문을 빠져나왔으므로 해당 좌표로는 갈 수 없기에 이전 좌표로 돌아가기
            nx -= dx[i]
            ny -= dy[i]

            if visited[nx][ny] == False:
                q.append((nx, ny, value + 1))
                visited[nx][ny] = True

    return -1

## 문제 풀이
# 뽀인트 : bfs로 미끄러지는거 생각해내기!