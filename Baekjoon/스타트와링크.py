## 백준 스타트와 링크 Silver1 https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

combis = list(combinations(list(range(n)),n//2))

answer = 1e9

for teama in combis:
    ta = 0
    tb = 0

    # 상대팀 인원 구하기
    teamb = []
    for i in range(n):
        if i not in teama:
            teamb.append(i)

    # a팀 능력치 합 구하기
    for i in teama:
        for j in teama:
            ta += board[i][j]

    # b팀 능력치 합 구하기
    for i in teamb:
        for j in teamb:
            tb += board[i][j]

    answer = min(answer, abs(ta-tb))

print(answer)

## input 1
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0
## output 1
# 0

## input 2
# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0
## output 2
# 2

## input 3
# 8
# 0 5 4 5 4 5 4 5
# 4 0 5 1 2 3 4 5
# 9 8 0 1 2 3 1 2
# 9 9 9 0 9 9 9 9
# 1 1 1 1 0 1 1 1
# 8 7 6 5 4 0 3 2
# 9 1 9 1 9 1 0 9
# 6 5 4 3 2 1 9 0

## output 3
# 1