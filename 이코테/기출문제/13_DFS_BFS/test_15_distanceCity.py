import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # 어디서 어디로 연결되어있는지 정보 저장

distance = [-1] * (n+1)
distance[x] = 0 # 출발도시는 최단거리 0

def bfs():
    q = deque()
    q.append(x)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1: # 최단거리 갱신이 안되어있다면
                distance[i] = distance[now] + 1 # 최단거리 갱신! (지금 위치에서 +1하면 된다. 거리는 1이니까)
                q.append(i) # 방문처리 된 노드를 큐에 삽입하기

    # 최단거리가 K인 노드가 존재하는지 아닌지 저장하는 변수
    isExist = False
    for i in range(1, n+1):
        if distance[i] == k: # 해당 노드의 최단거리가 K와 같다면
            print(i)
            isExist = True # 노드를 찾은거니까 True처리 해주기

    if isExist == False:
        print(-1)


bfs()