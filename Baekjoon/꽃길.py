## 백준 실버2 꽃길 - https://www.acmicpc.net/problem/14620
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def cal(positions):
    global answer
    visited = [] # 씨앗 혹은 꽃잎이 있는 자리인지 체크
    total = 0 # 총 드는 비용

    dx, dy = [1,-1,0,0], [0,0,1,-1] # 씨앗 기준으로 상하좌우로 꽃잎이 핀다
    for x, y in positions:
        if (x,y) in visited: # 씨앗이나 꽃잎이 핀 자리면 씨앗을 심을 수 없다. 바로 리턴해버리기
            return 1e9

        # 그런 경우가 아니라면 꽃잎을 뻗을 수 있는 자리인지 판단
        visited.append((x,y))
        total += board[x][y] # 씨앗 자리의 비용 더해주고

        # 꽃잎 체크해서 꽃잎 자리 비용 더해준다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) not in visited:
                visited.append((nx,ny))
                total += board[nx][ny]

            # 만약 꽃잎을 뻗을 수 없는 자리라면 즉시 리턴
            else:
                return 1e9
    return total

def solution():
    seed = [] # 씨앗을 심을 수 있는 좌표 모음 배열
    for i in range(1, n - 1): # 테두리에는 씨앗을 심을 수 없다
        for j in range(1, n - 1):
            seed.append((i, j))

    global answer
    answer = 1e9

    # 조합을 돌면서 심을 수 있는 위치들의 조합이면 값 비교해서 업데이트해주기
    for i in combinations(seed, 3):
        answer = min(answer,cal(i))

    print(answer)

solution()
## input
# 6
# 1 0 2 3 3 4
# 1 1 1 1 1 1
# 0 0 1 1 1 1
# 3 9 9 0 1 99
# 9 11 3 1 0 3
# 12 3 0 0 0 1
## output
# 12

## 문제 풀이
# 씨앗을 심을 수 있는 좌표를 따로 모아서 3가지 조합을 뽑은 후에 가능한 조합 중에서 가격 최소값을 구하기