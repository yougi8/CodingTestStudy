import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif maze[nx][ny] == 0: # 괴물이 있는 곳이면 가지 않기
                continue
            elif maze[nx][ny] == 1: # 아직 방문하지 않은 곳이면 가기
                maze[nx][ny] += maze[x][y]
                queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(0,0))
