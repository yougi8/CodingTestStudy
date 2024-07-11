# ## 프로그래머스 - 169199 리코쳇 로봇
# def solution(board):
#     answer = 0
#
#     rx, ry = 0, 0  # 말의 위치
#     gx, gy = 0, 0  # 목표지점의 위치
#
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 'R':
#                 rx, ry = i, j
#             elif board[i][j] == 'G':
#                 gx, gy = i, j
#
#     dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
#     visited = [[0] * len(board[0]) for i in range(len(board))]
#     visited[rx][ry] = 1
#
#     def dfs(x, y, answer):
#         if x == gx and y == gy:
#             return
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and visited[nx][ny] == 0:
#                 if nx == 0 or ny == 0:
#                     visited[nx][ny] = 1
#                     answer += 1
#                     dfs(nx, ny, answer)
#         return answer
#
#     # 경우의 수가 만들어지는지 판단
#     isPossible = 0
#     if gx == 0 or gy == 0:
#         isPossible = 1
#     for i in range(4):
#         if 0 <= gx + dx[i] < len(board) and 0 <= gy + dy[i] < len(board[0]):
#             if board[gx + dx[i]][gy + dy[i]] == 'D':
#                 isPossible = 1
#                 break
#
#     if isPossible == 1:
#         answer = dfs(rx, ry, answer)
#         return answer
#     else:
#         return -1