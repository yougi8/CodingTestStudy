# from collections import deque
#
#
# def solution(tickets):
#     answer = []
#
#     def bfs(idx):
#         result = []
#         # 티켓 사용했는지 확인 여부
#         visited = [False] * len(tickets)
#
#         queue = deque()
#         queue.append([tickets[idx][0], tickets[idx][1]])
#
#         visited[idx] = True
#
#         result.append(tickets[idx][0])
#         result.append(tickets[idx][1])
#         while queue:
#             start, end = queue.popleft()  # 출발지, 도착지
#
#             for i in range(len(tickets)):
#                 if end == tickets[i][0] and visited[i] != True:
#                     queue.append([tickets[i][0], tickets[i][1]])
#                     result.append(tickets[i][1])
#                     visited[i] = True
#                     break
#
#         for i in range(len(tickets)):
#             if visited[i] == False:
#                 return None
#
#         return result
#
#     for i in range(len(tickets)):
#         new_answer = bfs(i)
#
#         # 알파벳이 더 먼저인 결과를 출력하기
#         if new_answer != None and new_answer[0] == 'ICN':
#             if len(answer) == 0:
#                 answer = new_answer
#             for i in range(1,len(new_answer)):
#                 if new_answer[i] >= answer[i]:
#                     break
#                 else:
#                     answer = new_answer
#                     break
#     print(answer)
#
# solution([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "CCC"], ["CCC", "ICN"], ["ICN", "DDD"], ["DDD", "AAA"]])

from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 도착지를 알파벳 순으로 정렬 (역순으로 정렬해서, pop할 때는 a부터 나오게 함)
    for key in graph:
        graph[key].sort(reverse=True)

    route = []  # 여행경로 저장하는 리스트

    def dfs(node):
        # 출발지에 맵핑되는 도착지가 없어질 때까지 반복
        while graph[node]:
            next_node = graph[node].pop()  # 다음 출발지는 이전 노드의 도착지
            dfs(next_node)
        route.append(node)  # 더이상 갈 곳이 없을 때 경로에 추가

    dfs("ICN")  # ICN에서 시작
    return route[::-1]  # 거꾸로 출력