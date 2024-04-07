from collections import deque
n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = []
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1

    return

bfs(0,0)

print(graph)
print(graph[n-1][m-1])

## 문제 풀이
# dx범위랑 밑에 if문에서 ny대신 y로 오타가 났다.. 하.. 오타.. 제발 잘 보자
## input ex
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
## output : 10
