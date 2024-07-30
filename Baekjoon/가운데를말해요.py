## 백준 1655 - 가운데를 말해요 (heapq) https://www.acmicpc.net/problem/1655
import sys
import heapq

input = sys.stdin.readline
n = int(input())
left = []
right = []
for i in range(1,n+1):
    value = int(input())
    heapq.heappush(left, -value)
    heapq.heappush(right,-(heapq.heappop(left)))
    if len(left)<len(right):
        heapq.heappush(left,-(heapq.heappop(right)))
    print(-left[0])

# 입력  출력
# 7    1
# 1    1
# 5    2
# 2    2
# 10   2
# -99  2
# 7    2
# 5    5