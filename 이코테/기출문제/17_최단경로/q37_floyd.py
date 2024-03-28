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
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for k in range(1, n+1):
    for a in range(1, n+1):
        if a == k:
            continue
        for b in range(1, n+1):
            if b == k or a == b:
                continue
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

# 처음에는 아래 코드와같이 a,b가 k와 같다면 패스했다
# -> 뭔 뜻이냐면, 거쳐가는 노드(k)로 선택된 노드가 a,b값이 되지 않도록 해야한다고 생각
# -> ex) 노드가 1,2,3,4 일 때 1을 거쳐가는 상황이면, 23 24 32 34만 파악하면 되지 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44 다 볼  필요가 없다.
# 그래서 첨 생각한 코드
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         if a == k:
#             continue
#         for b in range(1, n+1):
#             if b == k or a == b:
#                 continue
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# 물론 이렇게 해도 되지만, 사실 min 비교하는데에서 항상 min값으로 선택될 것이기 때문에 굳이? 안해도 될 것 같다.