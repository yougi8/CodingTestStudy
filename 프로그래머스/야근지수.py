## 프로그래머스 - Lv3. 야근지수 https://school.programmers.co.kr/learn/courses/30/lessons/12927
import heapq

def solution(n, works):
    answer = 0
    q = []
    for work in works:
        heapq.heappush(q, -work)

    while n > 0:
        if len(q) == 0:
            break
        now = -heapq.heappop(q)
        now -= 1
        n -= 1
        if now > 0:
            heapq.heappush(q, -now)

    for tired in q:
        answer += tired ** 2
    return answer

## 문제 풀이
# heapify 사용하려고 했지만, 최대힙으로 구현해야 해서 직접 for문 돌면서 heapq에 집어 넣어줬다