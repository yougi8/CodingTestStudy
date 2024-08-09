## 프로그래머스 - 인사고과 https://school.programmers.co.kr/learn/courses/30/lessons/152995
## 해설 코드 (시간초과x)
# def solution(scores):
#     answer = 0
#     target_a, target_b = scores[0]
#     target_sum = target_a + target_b
#
#     scores.sort(key=lambda x:(-x[0],x[1]))
#     maxb = 0
#     for a, b in scores:
#         if target_a<a and target_b<b:
#             return -1
#
#         if a+b > target_sum:
#             if b>=maxb:
#                 answer += 1
#                 maxb = b
#
#     return answer+1
## 내 코드 (시간초과2문제)
def solution(scores):
    answer = 0

    for i in range(len(scores)):
        scores[i].append(i)
    sorted_score = sorted(scores, key=lambda x: (-x[0] - x[1], x[2]))

    # print(sorted_score)
    for i in range(len(sorted_score)):
        for j in range(i):
            if sorted_score[i][0] < sorted_score[j][0] and sorted_score[i][1] < sorted_score[j][1]:
                if sorted_score[i][2] == 0:
                    return -1
                answer -= 1
                break
        answer += 1

        if sorted_score[i][2] == 0:
            return answer

    return -1