## 백준 체스판 다시 칠하기 실버4 https://www.acmicpc.net/problem/1018
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = 1e9
# B : 1, W : 0
chess = []
for i in range(n):
    string = input().strip()
    arr = []
    for alpha in string:
        if alpha == 'B':
            arr.append(1)
        else:
            arr.append(0)
    chess.append(arr)
# print(chess)

for i in range(n-7):
    for j in range(m-7):
        result = [0, 0]
        # 시작이 1인 경우
        for x in range(8):
            for y in range(8):
                if (x+i)%2 == 0:
                    if (y+j)%2 == 0:
                        if chess[i+x][j+y] == 0:
                            result[0] += 1
                        else:
                            result[1] += 1
                    else:
                        if chess[i+x][j+y] == 1:
                            result[0] += 1
                        else:
                            result[1] += 1
                else:
                    if (y+j)%2 == 0:
                        if chess[i+x][j+y] == 1:
                            result[0] += 1
                        else:
                            result[1] += 1
                    else:
                        if chess[i+x][j+y] == 0:
                            result[0] += 1
                        else:
                            result[1] += 1
        answer = min(answer, result[0], result[1])
print(answer)



## input 1
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
## output1
# 1
## input2
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB
## output2
# 12
## input3
# 8 8
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
## output3
# 0