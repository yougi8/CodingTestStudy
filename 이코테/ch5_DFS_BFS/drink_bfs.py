## dfs 실전문제3 음료수 얼려먹기 - bfs코드
from collections import deque
n, m = map(int, input().split()) # 세로 n, 가로 m

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0

def bfs(x,y):
    if graph[x][y] == 1:
        return False

    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    while queue:
        x,y = queue.popleft()
        # print('x,y: ',x,y)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <=nx<=n-1 and 0<=ny<= m-1 and graph[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny] = 1

    return True

for i in range(n):
    for j in range(m):
        if bfs(i,j):
            answer += 1

print(answer)

### 문제 풀이
# queue에 집어넣고 방문처리를 안 해줘서 무한으로 돌았다.. ㅎ

## input ex
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
## output : 8