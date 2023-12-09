from collections import deque

def solution(maps):
    n = len(maps)  # 게임 맵의 행 개수
    m = len(maps[0])  # 게임 맵의 열 개수

    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return maps[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return -1

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
