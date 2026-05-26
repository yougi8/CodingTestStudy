## 프로그래머스 - 숫자의 표현 Lv.2 https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3

## 단순 O(n) 풀이법으로 풀어도 효율성 통과함. 혹은 투포인터로 해결할 수 있음.
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        total = 0
        
        for j in range(i, n+1):
            total += j
            if total==n:
                answer += 1
                break
            elif total>n:
                break
    return answer


## 아주아주 이상한 풀이..
# def solution(n):
#     answer = 0
#     flag = 1
    
#     while flag<=n:
#         sum = 0
#         time = 0
#         for i in range(flag, n+1):
#             sum += i
#             if sum < n:
#                 time += 1
#                 continue
#             elif sum == n:
#                 time += 1
#                 answer += 1
#                 if time%2 == 0:
#                     flag += time//2
#                 else:
#                     flag += (time+1)//2
#                 break
#             else:
#                 break
            
#         if time%2 == 0:
#             flag += time//2
#         else:
#             flag += (time+1)//2
        
        
#     return answer

print(solution(15))