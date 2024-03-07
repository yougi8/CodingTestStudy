## 백준 1697 숨바꼭질
from collections import deque

n, k = map(int, input().split()) ## 수빈이 위치, 동생 위치
max = 100000
visited = [0] * (max + 1) # 방문노드처리 (시간과 함께 기록 / 0으로 셋팅)

def bfs():
    q = deque() # 큐 생성
    q.append(n) # 수빈이 시작위치를 큐에 삽입
    while q:
        x = q.popleft() # 큐에서 하나 뽑은 값이 수빈이의 현재 위치
        direction = [x - 1, x + 1, x * 2] # 움직일 수 있는 경우의 수
        if x == k: # 수빈이의 현재 위치가 동생의 위치와 같다면
            print(visited[x]) # 해당 위치의 초를 print하고
            break # 종료
        for i in direction:
            if 0 <= i <= max and visited[i] == 0: # 이동한 위치가 범위내에 있고, 아직 방문하지 않았다면
                visited[i] = visited[x] + 1 #해당 위치를 x위치의 시간보다 1초 늘려주기!
                q.append(i) #방문했으니까 큐에 삽입

bfs()
