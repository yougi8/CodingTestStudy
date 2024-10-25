## 백준 골드5 로봇 청소기 https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 1:청소 완료, 0:청소 미완료
direction = [[1,0],[0,-1],[-1,0],[0,1]] # 후진을 기준으로 정렬 방법 명시 (북동남서)
dr, dc = [-1,1,0,0], [0,0,-1,1] # 반시계 방향으로 회전

answer = 0

while True:
    ## step1. 현재 칸이 청소되지 않았을 경우 청소
    if board[r][c] == 0:
        board[r][c] = -1
        answer += 1

    ## step2. 주변 4칸 청소여부 확인하기
    flag = True
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<=nr<n and 0<=nc<m:
            if board[nr][nc] == 0:
                flag = False
                break
    ## step3. 주변에 청소안된 칸이 없을 경우 후진한다
    if flag == True:
        nr, nc = r+direction[d][0], c+direction[d][1]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc]!=1:
            r,c = nr, nc
        else:
            break

    ## step4. 주변에 청소 안된 칸이 있을 경우 회전하고 앞칸이면 치운다
    else:
        d = (d+3)%4 # 반시계 방향으로 회전
        nr, nc = r-direction[d][0], c-direction[d][1]

        # 앞칸이 청소안되어 있으면 치운다
        if 0<=nr<n and 0<=nc<m and board[nr][nc]==0:
            board[nr][nc] = -1 # 치운 경우와 벽을 구분하기 위해 치운 경우는 -1로 표시
            answer += 1
            r,c = nr, nc

print(answer)

## input1
# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1
## output1
# 1
## input2
# 11 10
# 7 4 0
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 0 0 0 0 1
# 1 0 1 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1
## output2
# 57
