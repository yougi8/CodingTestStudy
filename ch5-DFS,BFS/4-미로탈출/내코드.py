from collections import deque
# n, m = map(int, input().split)
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
n, m =5, 6 # 답:10
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def bfs(x, y):
    result = 0

    graph[x][y] = 0 # (0,0) 출발점 방문처리
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft() # 현재 방문하고 있는 노드

        if x == n-1 and y == m-1:  # 만약 끝점에 도달한 경우
            return result  # 이동 횟수를 반환합니다.

        for i in range(4): # 상하좌우로 이동해 보기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m: # 예외 처리
                continue

            if graph[nx][ny] == 0: # 방문 했을 경우
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0 # 방문 처리
                result += 1

    return result
    # return graph[n-1][m-1]


print(bfs(0,0))

#####################################
# [오답]
## 1. queue에 graph[x][y]가 아니라 (x,y)를 저장해야 함!
## 2. 현재 result 변수는 단순히 이동 가능한 모든 위치의 수를 세고 있습니다.
##      그러나 이 문제에서 필요한 것은 시작점에서 끝점까지의 최소 이동 횟수이므로,
##      result 변수는 큐에 넣을 때마다 증가시키는 것이 아니라, 큐에서 위치를 꺼낼 때마다 증가시켜야 합니다.
###     ex) (1,2)에서 상 방향으로 이동 시, 최단거리가 아닌데도 result+1 됨.
## 3. result 변수를 따로 사용하지 않고 graph(x,y)에 result 값을 넣으면 간단히 될 일!


