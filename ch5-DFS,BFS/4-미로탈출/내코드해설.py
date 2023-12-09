from collections import deque

n, m = 5, 6
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
    queue = deque([(x, y, 1)])  # 현재 위치와 이동 횟수를 함께 저장

    while queue:
        x, y, result = queue.popleft()  # 현재 위치와 이동 횟수를 함께 꺼냄

        if x == n-1 and y == m-1:  # 만약 끝점에 도달한 경우
            return result  # 이동 횟수를 반환

        for i in range(4):  # 상하좌우로 이동해 보기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:  # 예외 처리
                continue

            if graph[nx][ny] == 1:  # 아직 방문하지 않은 위치라면
                queue.append((nx, ny, result + 1))  # 큐에 새로운 위치와 이동 횟수를 함께 저장
                graph[nx][ny] = 0  # 방문 처리

    return -1  # 만약 끝점에 도달할 수 없는 경우

print(bfs(0,0))
