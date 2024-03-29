## 이코테 chapter10 그래프 이론 - 10_6 위상정렬 알고리즘
### input 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
### output : 1 2 5 3 6 4 7
import sys
from collections import deque
## 노드 v, 간선 e
v, e = map(int, sys.stdin.readline().split())

## 진입차수 0으로 초기화
indegree = [0] * (v+1)

## 간선정보 담긴 그래프 초기화 & 값 저장
graph = [[] for _ in range(e)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    ## 진입차수 1 증가
    indegree[b] += 1

## 위상정렬 알고리즒
def topology_sort():
    ## 순서 저장하는 결과변수
    result = []

    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입하기
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        # 해당 노드에 연결된 간선 끊어주기 (진입차수 1씩 빼주기)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
