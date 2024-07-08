# ## 백준 아기상어 16236
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n = int(input())
# graph = []
#
# x,y = 0,0 # 아기상어의 위치
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] == 9:
#             x,y = i,j
#             graph[i][j] = -1
#
# def bfs(x,y):
#     dx, dy = [-1,1,0,0],[0,0,-1,1]
#     queue = deque((x,y))
#     visited = [[False] * n for _ in range(n)]
#
#     while queue:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0<=nx<n and 0<=ny<n and visited[nx][ny]:
#
#
# bfs(x,y)
#
