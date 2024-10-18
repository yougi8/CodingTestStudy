## 백준 암호 만들기 골드 5 - https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline
from itertools import combinations
l, c = map(int, input().split())
alphabets = list(map(str, input().split()))
answer = []
## step1. 자음/모음 구분하기
za = [] # 자음 배열
mo = [] # 모음 배열
for alphabet in alphabets:
    if alphabet in ['a','e','i','o','u']:
        mo.append(alphabet)
    else:
        za.append(alphabet)
mo.sort()
za.sort()
def check(str):
    cnt = 0
    for i in str:
        if i in ['a','e','i','o','u']:
            cnt += 1
    return cnt

## step2. 자음,모음 조합 사용하기
combi = list(combinations(alphabets,l))
for possible in combi:
    mo_int = check(possible)
    za_int = l - mo_int
    if mo_int<1 or za_int<2:
        continue
    else:
        result = sorted(possible)
        answer.append(''.join(result))
answer.sort()
for a in answer:
    print(a)


## input
# 4 6
# a t c i s w
## output
# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw

## 문제 풀이
# combinations list를 돌면서 뽑아낸 possible은 tuple 이므로 sort()가 되지 않는다.
# 처음에는 list(possible).sort() 이렇게 했지만 list로 형변환이 안됨!
# sorted(possible) 이렇게 하니까 됐다!
# tuple은 sorted 사용해야 하는 듯 하다