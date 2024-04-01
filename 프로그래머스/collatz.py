## 프로그래머스 연습문제 - 콜라츠 추측 (99클럽 비기너 문제) level 1
def solution(num):
    answer = 0
    while num != 1:
        if answer == 500:
            answer = -1
            break
        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = (num * 3) + 1
            answer += 1

    return answer