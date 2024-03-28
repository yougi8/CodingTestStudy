## 9-3 플로이드 워셜 알고리즘
# input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 n
n = int(input())
# 간선 개수 m
m = int(input())
# 연결정보 그래프 - 2차원 배열
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
# 간선에 대한 정보를 받아서 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 노드 n개만큼만 탐색하면 된다
for i in range(1, n+1):
    for a in range(1, n+1):
        if a == i:
            continue
        for b in range(1, n+1):
            if b == i:
                continue
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()