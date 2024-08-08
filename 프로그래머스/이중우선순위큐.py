## 프로그래머스 - 이중우선순위큐 https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for oper in operations:
        alpha = oper[0]
        num = int(oper[2:])

        if alpha == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            # 최솟값 삭제
            if num < 0 and min_heap:
                popped = heapq.heappop(min_heap)
                max_heap.remove(-popped)

            # 최댓값 삭제
            elif num >= 0 and max_heap:
                popped = -heapq.heappop(max_heap)
                min_heap.remove(popped)

    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    return [0, 0]