## 9-1 간단한 다익스트라 알고리즘
# input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
import sys
input = sys.stdin.readline
INF = int(1e9)

## 노드 n, 간선 m
n, m = map(int, input().split())
## 시작 노드
start = int(input())
## 노드, 간선 정보가 담긴 그래프
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
## 최단거리 테이블
distance = [INF] * (n+1)
## 방문기록
visited = [False] * (n+1)

## 현재 최단거리가 어떤 노드인지 알려주는 함수
def get_shortest():
    min_value = INF
    for i in range(1, n+1):
        if distance[i] < min_value and visited[i]==False:
            min_value = i
    return min_value

def dijkstra(start):
    distance[start] = 0 # 자기자신이니까 거리는 0
    visited[start] = True

    ## 시작점과 연결된 노드들의 최단거리 갱신해주기
    for i in graph[start]: # i는 (3,5) 이런식으로 할당된다. 노드 3까지 5만큼 거리. i[0]이 3, i[1]이 5
        distance[i[0]] = i[1]
    ## 시작노드 제외 나머지 노드들 살펴보기
    for i in range(n-1):
        min_node = get_shortest()
        visited[min_node] = True

        for j in graph[min_node]:
            value = distance[min_node] + j[1] # 지금 노드 값에서 이동할 간선 더한 값
            distance[j[0]] = min(distance[j[0]], value) # 기존에 있던 값과 value값 중 작은 값으로 선택

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

