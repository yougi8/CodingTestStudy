## 프로그래머스 - 부족한 금액 게산 (99클럽 미들러 문제) level 1

def solution(price, money, count):
    answer = 0

    pay = 0
    for i in range(1, count + 1):
        pay += price * i

    if pay >= money:
        answer = pay - money

    return answer