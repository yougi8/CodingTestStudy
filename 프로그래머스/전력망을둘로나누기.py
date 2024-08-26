## 프로그래머스 - 전력망을 둘로 나누기
from collections import deque
def solution(n, wires):
    answer = n

    def bfs(graph, x):
        result = 0
        visited = [False] * (n + 1)
        visited[x] = True
        q = deque([x])

        while q:
            wire = q.popleft()

            for i in graph[wire]:
                if visited[i] == False:
                    result += 1
                    visited[i] = True
                    q.append(i)
        return result

    for out in wires:
        graph = [[] * (n + 1) for _ in range(n + 1)]
        for wire in wires:
            if out == wire:
                continue
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])

        # 끊어진 애들 양쪽으로 살펴보면 된다
        first = bfs(graph, out[0])
        second = bfs(graph, out[1])
        answer = min(answer, abs(first - second))
    return answer
solution(4,[[1,2],[2,3],[3,4]])

## 문제 풀이
# 이어진 선들을 주어진 순서대로 제거해보는 경우를 모두 구한다.
# 예를 들어 (1,2)가 주어지면 1-2를 연결하는 선을 끊을 건데
# 1에서 시작하는 bfs 한 번, 2에서 시작하는 bfs를 한 번 돌고 그 값을 비교해서 넣어준다
# 그 중 최소값을 출력하면 된다