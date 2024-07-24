## 프로그래머스 석유시추

from collections import deque


def solution(land):
    n = len(land)  # 세로길이 n
    m = len(land[0])  # 가로길이 m
    visited = [[0] * m for _ in range(n)]
    result = [0] * m

    def bfs(a, b):
        q = deque()
        q.append((a, b))
        cnt = 0
        value = set([])
        value.add(b)
        while q:
            cnt += 1
            x, y = q.popleft()
            visited[x][y] = 1

            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0 and land[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        value.add(ny)
        return (value, cnt)

    for i in range(n):
        for j in range(m):
            # 방문하지 않았는데 석유가 존재할 때
            if visited[i][j] == 0 and land[i][j] == 1:
                position, size = bfs(i, j)
                # print(position,size)
                for k in position:
                    result[k] += size
                # print('result:',result)
    print(result)
    return max(result)

solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])