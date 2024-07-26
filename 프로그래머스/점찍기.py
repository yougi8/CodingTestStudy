## 프로그래머스 - 점찍기
from math import sqrt


def solution(k, d):
    answer = 0

    # for a in range(d//k+1):
    #     for b in range(d//k+1):
    #         now = (a*k)**2+(b*k)**2
    #         if now>d**2:
    #             break
    #         answer += 1

    for x in range(d // k + 1):
        b = sqrt(d ** 2 - (x * k) ** 2)
        answer += int(b) // k + 1
    return answer

## 처음에 : a, b 를 0부터 ~~까지해서 이중for문으로 했는데 시간초과나서 50%만 정답
## 그림 그려서 생각해보니까 규칙?같은게 있었음!