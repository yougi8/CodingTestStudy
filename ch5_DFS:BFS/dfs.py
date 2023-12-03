def dfs(graph, v, visited):
    visited[v] = True ## 방문한 노드의 상태값 True로 바꿔주기
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

visited = [False] * 9 ## 방문상태는 false로 초기화

dfs(graph, 1, visited)
