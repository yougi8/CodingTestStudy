## 백준 - 주식 https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):

    n = int(input())
    price = list(map(int, input().split()))

    result = 0

    max_value = 0
    for i in range(n-1, -1, -1):
        if price[i] > max_value:
            max_value = price[i]
        else:
            result += max_value - price[i]

    print(result)

# T = int(input())
# for _ in range(T):
#     day = int(input())
#     days = list(map(int, input().split(' ')))
#
#     idx = 0
#     answer = 0
#     max_value = -1
#     max_idx = 0
#     buy = []
#     heapq.heappush(buy,days[0])
#     for i in range(len(days)):
#         if days[i]>=max_value:
#             max_value = days[i]
#             max_idx = i
#
#     already = []
#     cnt = 0
#     for i in range(1,len(days)):
#         if days[i]>=days[i-1] and i>=max_idx:
#             for j in range(len(buy)):
#                 price = heapq.heappop(buy)
#                 if price<days[i] and i not in already:
#                     answer += days[i]-price
#                 already.append(cnt+j)
#             cnt += 1
#         else:
#             heapq.heappush(buy,days[i])
#     print(answer)




## 예제 입력 1
# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2
## 예제 출력 1
# 0
# 10
# 5