def solution(a, b):
    answer = 0
    if a < b:
        answer = sum(list(range(a, b+1)))
    else:
        answer = sum(list(range(b, a+1)))
    return answer

## max, min 사용 풀이법
# def solution(a, b):
#     answer = 0
#     for i in range(min(a,b), max(a,b)+1):
#         answer += i
#     return answer