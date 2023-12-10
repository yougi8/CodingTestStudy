## 백 1012 유기농 배추
import sys
sys.setrecursionlimit(10000)  # 재귀 제한 늘려주기

t = int(sys.stdin.readline()) # 테스트 케이스 개수
 ## T번만큼 진행
for time in range(t):
    m, n, k = map(int, sys.stdin.readline().split())  # 가로, 세로, 배추 위치
    graph = [[0]*m for _ in range(n)] # 배추가 심어져있는 그래프
    pos = [] # 배추 위치 저장할 배열
    for i in range(k):
        pos = list(map(int, sys.stdin.readline().split()))
        graph[pos[1]][pos[0]] = 1 # 단단히 속았다. X값이 위아래 이동이 아니고 좌우이동하는 값이었다.

    result = 0
    dx = [-1, 1, 0, 0] # 상하좌우 탐색
    dy = [0, 0, -1, 1] # 상하좌우 탐색
    def dfs(x,y):
        # 확인하고자 하는 위치가 밭 밖으로 나가면 즉시 false return
        if x <= -1 or x >=n or y <= -1 or y >= m:
            return False
        # 아직 방문하지 않은 곳이라면! 살펴봐야됨.
        if graph[x][y] == 1:
            # 방문처리해주고
            graph[x][y] = 0
            # 상하좌우에 대해서 방문하면서 확인!
            for i in range(4):
                dfs(x+dx[i], y+dy[i])
            return True
        return False

    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                result += 1
    print(result)