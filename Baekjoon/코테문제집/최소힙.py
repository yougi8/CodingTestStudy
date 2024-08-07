## 백준 - 최소 힙 https://www.acmicpc.net/problem/1927
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    x = int(input())
    if x==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,x)

## 예제 입력 1
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
## 예제 출력 1
# 0
# 1
# 2
# 12345678
# 0