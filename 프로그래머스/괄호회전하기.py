## 프로그래머스 Lv.2 - 괄호 회전하기 https://school.programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque

def is_possible(q):
    
    stack = []
    mapping = {'}':'{', ']':'[', ')':'('}
    
    for char in q:
        # 여는 괄호인 경우, stack에 추가
        if char in '({[':
            stack.append(char)
        
        # 닫는 괄호인 경우, 짝이 맞는지 확인하기
        else:
            # 여는 괄호가 없거나, 마지막에 들어간 여는 괄호와, 현재 닫는 괄호가 일치하지 않으면
            if not stack or stack[-1] != mapping[char]:
                return 0 # 올바르지 않음
            # 여는 괄호와 닫는 괄호가 일치한다면 짝지어서 여는 괄호 꺼내주기
            else:
                stack.pop()
    if len(stack) == 0:
        return 1

def solution(s):
    answer = 0
    q = deque(s)
    
    for _ in range(len(s)):
        if is_possible(q):
            answer += 1
        q.rotate(-1) # 왼쪽으로 한칸씩 밀기
    return answer

## 짝지어 회전하기 문제와 유사함.
## 괄호 매칭 == 스택 국룰