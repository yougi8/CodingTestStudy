## 프로그래머스 - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    test = heapq.heappop(scoville)
    if test >= K:
        return answer
    else:
        heapq.heappush(scoville, test)

    while len(scoville) >= 2:
        answer += 1
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, one + two)

        test = heapq.heappop(scoville)
        if test >= K:
            return answer
        else:
            heapq.heappush(scoville, test)
    return -1

## 문제 풀이
# test>=K 검증하는 부분을 while문 안에다가만 넣어놓으면
# 테스트케이스 18번이 통과가 안된다.
# 추측으로는, scoville의 길이가 처음부터 2인데, 처음부터 둘 다 K가 넘는 경우인 것 같다 -> 안 섞어도 목표 도달이니까 0 리턴!
# 그래서 그 검증 부분을 while문 밖에다가도 하나 둬서 들어오자마자 바로 검증할 수 있도록!

## 개선 코드 - pop-push 과정을 while문 반복할 때마다 하니까 그게 시간을 많이 잡아먹음! 너무너무 비효율적. 그냥 [0]번째 값만 비교해도 됨
# import heapq
#
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)
#
#     while scoville[0]<K:
#         if len(scoville)<2:
#             return -1
#         one = heapq.heappop(scoville)
#         two = heapq.heappop(scoville)*2
#         heapq.heappush(scoville,one+two)
#         answer += 1
#     return answer