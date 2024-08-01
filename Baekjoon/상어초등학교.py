## 백준 - 상어 초등학교 https://www.acmicpc.net/problem/21608

import sys
input = sys.stdin.readline

n = int(input())
board = [[] for _ in range(n**2+1)] # 학생 선호도 기록 (학생 번호 순서대로..)
flow = [] # 학생 입력받은 순서 기록
global result
for i in range(1, n**2+1):
    info = list(map(int, input().split(' ')))
    board[info[0]].append(info)
    flow.append(info[0])

seat = [[0]*n for _ in range(n)]

def search(student):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    able = []

    for x in range(n):
        for y in range(n):
            # 비어있는 자리면 앉을 수 있는 후보니까 자리의 가치? 판단 시작
            if seat[x][y] == 0:
                empty = 0 # 빈자리 수
                like = 0 # 좋아하는 친구 수
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        if seat[nx][ny] in board[student][0][1:]:
                            like += 1
                        if seat[nx][ny] == 0:
                            empty += 1
                able.append([like,empty,x,y])
    able.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    seat[able[0][2]][able[0][3]] = student
    return

# 선호도 계산
def cal():
    global result
    result = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    for x in range(n):
        for y in range(n):
            like = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if seat[nx][ny] in board[seat[x][y]][0][1:]:
                        like += 1
            if like != 0:
                result += 10**(like-1)
    return

for i in range(n**2):
    search(flow[i])

cal()
print(result)

## 풀이과정
# 처음에 seat 배열을 굳이굳이 n+1로 했는데, 그럴 필요가 없다. 학생 번호와는 상관없는 배열이기 때문
# 그리고 학생선호도가 담긴 배열을 학생 번호순서대로 하려다보니 이 배열과 별개로 학생 번호 입력받는 순서를 기록한 배열을 따로 만들었는데
# 그럴필요 전혀 없음. 메모리 낭비! & 코드 복잡해짐

# 예제 입력 1      예제 출력
# 3               54
# 4 2 5 1 7
# 3 1 9 4 5
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4

# 예제 입력 2      예제 출력
# 3               1053
# 4 2 5 1 7
# 2 1 9 4 5
# 5 8 1 4 3
# 1 2 9 3 4
# 7 2 3 4 8
# 9 8 4 5 7
# 6 5 2 3 4
# 8 4 9 2 1
# 3 9 2 1 4