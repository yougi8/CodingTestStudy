## 프로그래머스 - 실습 - 딕셔너리(해시맵) - 의상

from collections import defaultdict

def solution(clothes):
    answer = 1

    dic = defaultdict(list)
    for value, key in clothes:
        dic[key].append(value)
    for value in dic:
        answer *= (len(dic[value]) + 1)

    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

## 문제 풀이
# 종류별로 가지고 있는 가지수를 모두 곱한 값이 답이다!
# 그치만 해당 종류를 아예 선택 안 하는 경우도 있기 때문에, 가지수 + 1 값을 곱해야 한다.
# 그리고 answer 낼 때, 모두 다 선택 안 하는 경우 1을 뺀 게 답!