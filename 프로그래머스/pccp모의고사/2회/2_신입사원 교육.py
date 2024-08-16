import heapq
# 5분 소요
def solution(ability, number):
    heapq.heapify(ability)
    for i in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability,a+b)
        heapq.heappush(ability,a+b)
    answer = sum(ability)
    return answer

## 전형적인 heapq문제