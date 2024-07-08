import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()

    max_value = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    if graph[nx][ny] > max_value:
                        max_value = graph[nx][ny]
                    queue.append((nx,ny))

    return max_value

max_value = bfs(0,0)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)

if max_value == 0:
    print(0)
else:
    print(max_value - 1)