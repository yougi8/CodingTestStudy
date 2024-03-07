## 백준 5014 스타트링크
from collections import deque
f, s, g, u, d = map(int, input().split()) # 총, 강호, 회사, 업, 다운
visited = [0] * (f+1) # 방문기록
count = [0] * (f+1) # 카운트 기록

def bfs():
    visited[s] = 1 # 시작 위치는 방문처리
    stairs = 0
    q = deque([s]) # 강호의 시작 위치 큐에 삽입
    while q:
        x = q.popleft()
        if x == g:
            print(count[x])
            stairs = 1
            break
        direction = [x+u, x-d] # 이동 가능한 경우
        for i in direction:
            if 1 <= i <= f and visited[i] == 0: # 이동한 위치가 건물 범위 내에 있고, 방문하지 않은 노드라면
                q.append(i)
                visited[i] = 1
                count[i] = count[x]+1
    if stairs == 0:
        print("use the stairs")


bfs()
