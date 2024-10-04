## 프로그래머스 Lv2. 배달 https://school.programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
import heapq


def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [1e9] * (N + 1)
    distance[1] = 0

    hq = [(0, 1)]

    while hq:
        cost, x = heapq.heappop(hq)

        # 이미 최단경로 구한 적 있었으면 패스
        if distance[x] < cost:
            continue

        for node, dis in graph[x]:
            d = dis + cost

            if distance[node] > d:
                distance[node] = d
                heapq.heappush(hq, (d, node))

    for d in distance[1:]:
        if d <= K:
            answer += 1
    return answer

## 문제 풀이
# 전형적인 다익스트라 문제. deque를 사용해서 풀어도 되지만, heapq를 사용해서 풀어도 된다!
## 절반만 통과되는 코드
# def solution(N, road, K):
#     answer = 1
#     arr = [[10000] * (N + 1) for _ in range(N + 1)]
#
#     for a, b, c in road:
#         arr[a][b] = min(c, arr[a][b])
#         arr[b][a] = arr[a][b]
#
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if i == j: continue
#             for k in range(1, N + 1):
#                 if k == i or k == j: continue
#
#                 arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
#                 arr[j][i] = arr[i][j]
#
#     for i in range(2, N + 1):
#         if arr[1][i] <= K:
#             answer += 1
#     return answer