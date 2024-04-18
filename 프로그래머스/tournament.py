## 프로그래머스 - 예상 대진표 (프로그래머스 Lv.2) 99미들러문제
def solution(n, a, b):
    answer = 0
    while True:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1
        if a == b:
            break

    return answer
## 문제 풀이
# - 2로 나누었을때의 몫과 나머지를 합한 값이 같은 숫자들끼리 대결상대임!
# - 그래서 a,b가 그 값들이 같을 때까지, 즉, 같은 대진 안에 들어올 때까지 while문 실행