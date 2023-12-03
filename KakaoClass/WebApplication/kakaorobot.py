from collections import deque
def move(pos, board):
    nxt_pos= [] # 이동 가능한 위치들
    pos = list(pos) # 집합형태의 pos를 리스트 형식으로 변환

    # 현재 위치한 좌표값들 저장하기
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 방법1 : 상,하,좌,우 평행이동
    dx = [-1,1,0,0] # 상하좌우 각 이동 경우에 대해 처리.
    dy = [0,0,-1,1]
    for i in range(4): # 상,하,좌,우 네가지 경우 확인해보기
        nx1_x, nx1_y, nx2_x, nx2_y = pos1_x+dx[i], pos1_y+dy[i],pos2_x+dx[i], pos2_y+dy[i]
        if board[nx1_x][nx1_y] == 0 and board[nx2_x][nx2_y] == 0: # 이동하고자 하는 곳이 비어있는, 이동 가능한 곳이라면
            nxt_pos.append({(nx1_x, nx1_y), (nx2_x, nx2_y)}) # 이동 가능한 위치에 추가하기!

    # 방법2 : 회전
    # 로봇이 가로방향으로 놓여져있을 때
    if pos1_x == pos2_x:
        UP, DOWN = -1, 1 # 위로 회전 혹은 아래로 회전. 좌표값이니까 위로 회전하고싶을 땐 index-1로 위쪽 확인, 아래로 회전하고싶을 땐 index+1로 아래쪽 확인
        for d in [UP, DOWN]:
            if board[pos1_x + d][pos1_y] == 0 and board[pos2_x + d][pos2_y] == 0: # 위쪽 두칸 모두 혹은 아래쪽 두칸 모두가 0이라면 이동 가능!
                nxt_pos.append({(pos1_x, pos1_y), (pos1_x+d, pos1_y)}) # 이동가능 집합에 추가(위로 이동했는지 아래로 이동했는지까지!
                nxt_pos.append({(pos2_x, pos2_y), (pos2_x+d, pos2_y)})

    # 세로 방향으로 놓여져있을 때
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if board[pos1_x][pos1_y+d] == 0 and board[pos2_x][pos2_y+d] == 0: # 왼쪽 두칸 모두 혹은 오른쪽 두칸 모두가 0이라면 이동 가능!
                nxt_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+d)}) # 이동가능 집합에 추가(왼쪽으로 이동했는지 오른쪽으로 이동했는지까지!
                nxt_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+d)})

    return nxt_pos


def solution(board):
    # 로봇이 맵을 벗어나는지 판단을 더 간단히 하기 위해 맵 외곽에 벽 세우기
    n = len(board) # 맵의 크기 : n*n
    new_board = [[1] * (n + 2) for _ in range(n + 2)] ## 맵 외곽에 1을 추가하여 벽 쌓기
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j] ## 기존 맵 복사

    q = deque() # 로봇의 좌표와 걸리는 시간 저장
    visited = [] # 방문 확인용
    pos = {(1, 1), (1, 2)} # 현재 로봇이 위치한 좌표
    q.append((pos, 0)) # 시작지점의 좌표와 시간 입력
    visited.append(pos) # 시작지점 방문처리


    while q:
        pos, cost = q.popleft()
        if (n, n) in pos : # 현재 로봇이 있는 위치가 끝지점(도착해야하는 위치)이라면
            print('로봇이 (N,N)까지 이동하는데 필요한 최소 시간 : ',cost)
            return cost #도착! 그동안의 시간값 반환

        # 이동 가능한 좌표들의 리스트만큼 cost 계산
        for nxt in move(pos, new_board):
            if nxt not in visited:
                q.append((nxt, cost + 1))
                visited.append(nxt)

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print('input board : ',board)
solution(board)