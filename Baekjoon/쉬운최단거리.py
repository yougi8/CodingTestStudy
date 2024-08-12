## 백준 - 쉬운 최단거리 https://www.acmicpc.net/problem/14940
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]
start = [-1,-1]
for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            start[0] = i
            start[1] = j
            break
    if start[0]==i and start[1]==j:
        break

def bfs(x,y):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    board[x][y] = 0
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and board[nx][ny]!=0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1

bfs(start[0],start[1])
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            if visited[i][j]==0:
                print(-1, end=' ')
            else:
                print(board[i][j],end=' ')
        else:
            print(board[i][j], end=' ')
    print()

## 시간 약간 개선 코드
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# board = []
# for i in range(n):
#     board.append(list(map(int, input().split())))
# visited = [[-1]*m for _ in range(n)]
# start = [-1,-1]
# for i in range(n):
#     for j in range(m):
#         if board[i][j]==2:
#             start[0] = i
#             start[1] = j
#             break
#     if start[0]==i and start[1]==j:
#         break
#
# def bfs(x,y):
#     dx, dy = [-1,1,0,0], [0,0,-1,1]
#     visited[x][y] = 0
#     q = deque()
#     q.append((x,y))
#
#     while q:
#         x,y = q.popleft()
#
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#
#             if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
#                 if board[nx][ny]==0:
#                     visited[nx][ny]=0
#                 else:
#                     q.append((nx,ny))
#                     visited[nx][ny] = visited[x][y] + 1
#
# bfs(start[0],start[1])
# for i in range(n):
#     for j in range(m):
#         if board[i][j]==0:
#             print(0,end=' ')
#         else:
#             print(visited[i][j], end=' ')
#     print()

## 예제 입력 1
# 15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

## 예제 출력 1
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
# 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# 11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
# 12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
# 13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
# 14 15 16 17 18 19 20 21 22 23 0 31 32 33 34