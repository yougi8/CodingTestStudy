## 프로그래머스 - 가장 먼 노드 Lv.3 https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def solution(n, vertex):
    answer = [0] * (n + 1) # 1로부터의 거리를 저장
    graph = [[] * (n + 1) for _ in range(n + 1)] # 연결정보 저장 (graph[1]은 1이랑 연결되어있는 노드들을 가지고 있고, graph[2]는 2랑 연결되어 있는 노드번호를 가지고 있다.)

    # 연결정보 저장
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1) # bfs로 살펴봤는지 아닌지 판단
    q = deque([1]) # 1부터 탐색 시작

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == False:
                answer[i] = answer[node] + 1
                q.append(i)
                visited[i] = True
    return answer[2:].count(max(answer))

## BFS 인접노드 방식