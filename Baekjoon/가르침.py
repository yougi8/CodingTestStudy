## 백준 골드4 가르침 https://www.acmicpc.net/problem/1062
import sys
from itertools import combinations
input = sys.stdin.readline

n,k = map(int, input().split())
words = [set(input().strip()) for _ in range(n)]

if k<5: # antic은 반드시 나오니까 5개는 가르쳐야 함.
    print(0)
elif k>=26: # k가 알파벳 개수보다 많으면 주어진 단어를 무조건 다 읽을 수 있음
    print(n)
else:
    essential = {'a', 'n', 't', 'i', 'c'}
    answer = 0
    arr = set() # antic을 제외한 알파벳 집합
    for word in words:
        arr.update(word-essential)

    learn = list(arr)
    re = min(k-5,len(learn))
    combis = combinations(learn,re)
    # print(arr)
    for combi in combis:
        # print(combi)
        lst = list(combi) + list(essential)
        result = 0
        for word in words:
            # for x in word:
            #     if x not in combi and x!='a' and x!='n' and x!='t' and x!='i' and x!='c':
            #     # if x not in lst:
            #         break
            if all(char in lst for char in word):
                result += 1
            # else:
            #     result += 1
        answer = max(answer,result)
    print(answer)

## input1
# 3 6
# antarctica
# antahellotica
# antacartica
## output1
# 2
## input2
# 2 3
# antaxxxxxxxtica
# antarctica
## output2
# 0
## input3
# 9 8
# antabtica
# antaxtica
# antadtica
# antaetica
# antaftica
# antagtica
# antahtica
# antajtica
# antaktica
## output3
# 3
