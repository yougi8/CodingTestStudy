## 백준 18405, 이코테 기춝문제 17. 경쟁적 전염 - dfs/bfs
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split()) # nxn크기의 시험관, k가지의 바이러스
graph = []
virus_data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus_data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 몇 초인지, x좌표, y좌표 저장
ts, tx, ty = map(int, input().split()) # s초 후에 x,y 위치에 있는 바이러스 종류

virus_data.sort()

queue = deque(virus_data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    virus, s, x, y = queue.popleft()
    if s == ts:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
            graph[nx][ny] = virus
            queue.append((virus, s+1, nx, ny))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


print(graph[tx-1][ty-1])
## input ex
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2