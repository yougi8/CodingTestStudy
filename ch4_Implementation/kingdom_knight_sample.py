import sys
input_value = sys.stdin.readline()

row = int(input_value[1])
column = int(ord(input_value[0]) - ord('a')) + 1 ## ord() : 아스키 코드 값 반환. 여기서는 a를 기준으로.

steps = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

total = 0
for step in steps:
    if row+step[0]>=1 and row+step[0]<=8 and column+step[1]>=1 and column+step[1]<=8:
        total += 1
print(total)