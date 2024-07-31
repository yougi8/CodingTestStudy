## 프로그래머스 - 게임 맵 최단거리 (bfs)
from collections import deque


def bfs(x, y, maps, n, m):
    q = deque()
    q.append((x, y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] += maps[x][y]
    return maps[n - 1][m - 1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = bfs(0, 0, maps, n, m)
    if answer == 1:
        return -1
    else:
        return answer
