# bfs
from collections import deque
def solution(maps):

    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0] # 상 하 좌 우
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        if x == len(maps)-1 and y == len(maps[0])-1:
            return maps[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                # print('(x,y), count:', nx, ny, maps[nx][ny])

    return -1



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(maps))