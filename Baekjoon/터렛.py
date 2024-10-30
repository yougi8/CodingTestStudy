## 백준 silver3 터렛 https://www.acmicpc.net/problem/1002
import sys
import math
input = sys.stdin.readline
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif d == r1+r2 or d == abs(r1-r2): # 외접 혹은 내접
        print(1)
    elif abs(r1-r2) < d < r1+r2: # 겹침
        print(2)
    else:
        print(0)

## 문제 풀이
# 원이 한 점에서 만나면 1, 완벽히 겹치면 -1, 두 점에서 만나면 2, 품고 있거나 안 만나면 0
# # input
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5
## output
# 2
# 1
# 0