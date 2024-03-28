## 기출문제 - 최단경로 q37 플로이드
# input
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 n (노드)
n = int(input())
# 버스의 개수 m (간선)
m = int(input())
# 간선정보 저장 그래프 (2차원 배열)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 그래프 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # A->B를 잇는 간선이 2개 이상일 수 있기 때문에, 혹시 이전에 값이 들어와있다면 비교해서 작은 값으로 반영해야한다.

# 자기자신으로 가는 것은 0
for i in range(1, n+1):
    graph[i][i] = 0

# a->b와 a->k->b 중에서 더 최단거리를 기록하기
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('0', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

## 풀이 정리
# - 플로이드워셜 알고리즘을 사용하면 된다.
# - 다만, 간선정보를 저장할 때, 간선이 하나 이상일 수 있기 때문에 무조건 다 저장하는 것이 아니라 이미 저장되어있는 값과 비교해서 작은 값으로 반영해야한다!
# - 이 부분을 처음에는 몰라서 몇몇 값이 좀 크게 나왔당