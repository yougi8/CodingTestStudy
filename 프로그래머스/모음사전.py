## 프로그래머스 모음사전 LV2
from itertools import product

def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dic = []

    for i in range(1, 6):
        combi = list(product(alphabet, repeat=i))
        for j in combi:
            dic.append(''.join(j))
    dic.sort()

    answer = dic.index(word) + 1
    return answer

## 문제 풀이
# 완전탐색 문제 + 길이가 별로 크지 않아서 중복순열 product를 사용해서 무식하게 풀었다.
