## 프로그래머스 Lv3. 경주로 건설 https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque


def solution(board):
    def bfs(start):
        n = len(board)
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 오 아래 왼 위 0 1 2 3

        visited = [[1e9] * (n) for _ in range(n)]
        visited[0][0] = 0

        q = deque()
        q.append(start)  # x좌표, y좌표, 방향, 최솟값

        while q:
            x, y, direction, value = q.popleft()

            for i in range(4):
                total = value
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    if i == direction:
                        total += 100
                    else:
                        total += 600

                    if total <= visited[nx][ny]:
                        q.append((nx, ny, i, total))
                        visited[nx][ny] = total

        return visited[-1][-1]

    return min(bfs((0, 0, 0, 0)), bfs((0, 0, 1, 0)))