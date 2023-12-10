## 백준 7562 나이트의 이동
import sys
from collections import deque
t = int(sys.stdin.readline()) # 테스트 케이스의 개수

for i in range(t):
    l = int(sys.stdin.readline()) # 체스판의 한 변의 길이 (크기는 l*l)
    now = list(map(int, sys.stdin.readline().split()))
    goal = list(map(int, sys.stdin.readline().split()))
    graph = [[0]*l for _ in range(l)] # 체스판
    visited = [[False] * l for _ in range(l)]  # 방문처리

    # 나이트가 이동할 수 있는 방향
    moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)] # 시계방향으로

    def bfs():
        queue = deque()
        queue.append(now)
        visited[now[0]][now[1]] = True
        while queue:
            x, y = queue.popleft()

            if x == goal[0] and y == goal[1]:
                return graph[x][y]

            for i in range(8):
                nx, ny = x+moves[i][0], y+moves[i][1]

                if nx<=-1 or nx>=l or ny<=-1 or ny>=l: # 체스판 밖으로 나가면 안됨
                    continue
                if visited[nx][ny] is False:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

    print(bfs())
