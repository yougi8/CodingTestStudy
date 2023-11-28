from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) ## bfs 구현 위해서 큐 자료구조 사용

    visited[start] = True ## 방문노드상태 True처리

    while queue:
        v = queue.popleft() ## 먼저 삽입된 값 출력
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph=[
    [], ## 노드 번호를 1부터 시작하는 것으로 설정했기 때문에, 인덱스 0번은 비워두기!
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
