## 백준 7576 토마토
from collections import deque
import sys

m,n = map(int, sys.stdin.readline().split()) # 상자 크기 m x n (가로 x 세로) min: 2, max: 1000
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 토마토 위치 담긴 배열 (0,1,-1)

## 이동하는 좌표 : 상,하,좌,우
dx, dy = [-1,1,0,0], [0,0,-1,1]
q = deque([])

result = 0 # 며칠 걸리는지 저장하는 변수

# 익은 토마토가 있는 위치만 큐에 넣어준다. 좌표로!
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4): # 상하좌우로 가면서
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny]==0: # 범위에 벗어나지 않고, 안익은 토마토가 있다면
                q.append([nx,ny]) # 큐에 추가!
                box[nx][ny] = box[x][y]+1 # 하루 뒤에 익으니까 +1
bfs()

for i in box:
    for j in i:
        if j==0: # 순회를 다 했는데도 안 익은 토마토가 발견된다면
            print(-1) # -1 출력
            exit(0) # 그리고 코드 종료
    # 그렇지 않다면 최대값 구해주기
    if max(i) > result:
        result = max(i)
# 처음 시작을 1로 했으니까 1 빼주기! 만나이같은 개념..
print(result-1)