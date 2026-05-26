## 프로그래머스 - 짝지어 제거하기 Lv.2 https://school.programmers.co.kr/learn/courses/30/lessons/12973

# 스택을 이용해서 풀이. O(n) 시간복잡도.
# 스택이 비어있지 않게끔 문자열을 집어넣고. 그 스택 안의 문자열이랑 비교해서 같으면 스택에 추가하지 않음. 그리고 스택에 들어있던 문자열을 제거
# 그러면 중복되는 두개를 다 제거할 수 있게 됨.
def solution(s):
    answer = 0
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0


## 절반정도 시간초과 : 문자열 슬라이싱 할 때 O(n^2) 되가지고 .. 
# def solution(s):
#     answer = 0
#     new_str = s
#     i = 0
    
#     while i<len(new_str)-1:
#         length = len(new_str)

#         if new_str[i] == new_str[i+1]:
#             if length == 2:
#                 return 1
#             elif i == 0:
#                 new_str = new_str[i+2:length]
#             else:
#                 new_str = new_str[0:i] + new_str[i+2:length]
#             i = 0
#         else:
#             i += 1
    
#     return 0

solution("baabaa")