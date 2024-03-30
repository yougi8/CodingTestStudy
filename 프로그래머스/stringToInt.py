## 프로그래머스 - 문자열을 정수로 바꾸기 (99클럽 비기너 문제) level 1
def solution(s):
    answer = 0
    if s[1] == '-':
        answer = int(s) * (-1)
    else:
        answer = int(s)
    return answer