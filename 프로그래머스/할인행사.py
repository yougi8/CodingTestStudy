## 프로그래머스 - 할인 행사 https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import defaultdict

def solution(want, number, discount):
    answer = 0

    dic = defaultdict(list)
    for i, food in enumerate(want):
        count = number[i]
        dic[food] = count

    for i in range(len(discount)):
        cnt = 0
        j = i
        dic2 = defaultdict(list)
        while cnt < 10 and j < len(discount):
            dic2[discount[j]].append(1)
            j += 1
            cnt += 1
        for k in range(len(want)):
            if dic[want[k]] != len(dic2[want[k]]):
                break
            if k == len(want) - 1:
                answer += 1
    return answer

## 풀이
# 코드가 딱 봐도 더러운데, 실제로 엄청 느리게 동작한다!
# 다음에 풀 땐 좀 더 빠르게 깔끔하게 풀어봐야겠다