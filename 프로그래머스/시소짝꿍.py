## 프로그래머스 - 시소짝꿍 Lv.2 https://school.programmers.co.kr/learn/courses/30/lessons/152996
def solution(weights):
    answer = 0
    dic = {}

    for weight in weights:
        if weight in dic:
            dic[weight] += 1
        else:
            dic[weight] = 1

    for weight in dic:
        # 원래 무게가 같은 사람(두번이상 추가되었을 것임 == 값이 2 이상)
        if dic[weight] >= 2:
            answer += (dic[weight]) * (dic[weight] - 1) / 2
        # 무게 비율이 1:2
        if (weight * 2) in dic:
            answer += dic[weight] * dic[weight * 2]
        if (weight * 2 / 3) in dic:
            answer += dic[weight] * dic[weight * 2 / 3]
        if (weight * 3 / 4) in dic:
            answer += dic[weight] * dic[weight * 3 / 4]

    return answer

solution([100,180,360,100,270])

# 대실패코드
# import heapq
# from collections import defaultdict

# def solution(weights):
#     answer = 0
#     N = len(weights)
#     q = []
#     for i in range(N):
#         heapq.heappush(q, (weights[i], i))
#         heapq.heappush(q, (weights[i] * 2, i))
#         heapq.heappush(q, (weights[i] * 3, i))
#         heapq.heappush(q, (weights[i] * 4, i))

#     added = defaultdict(list)
#     for i in range(len(q)-1):
#         value, idx = heapq.heappop(q)
#         cnt = 0
#         while cnt<len(q):
#             if value == q[cnt][0]:
#                 if idx != q[cnt][1] and idx not in added[q[cnt][1]]:
#                     added[idx].append(q[cnt][1])
#                     added[q[cnt][1]].append(idx)
#                     answer += 1
#             else:
#                 break
#             cnt += 1
#     return answer