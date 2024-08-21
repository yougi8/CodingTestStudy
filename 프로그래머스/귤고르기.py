## 프로그래머스 - 귤 고르기 Lv2 https://school.programmers.co.kr/learn/courses/30/lessons/138476
import heapq

def solution(k, tangerine):
    answer = 0
    fruits = {}
    for size in tangerine:
        if size in fruits:
            fruits[size] += 1
        else:
            fruits[size] = 1

    q = []
    for key, value in fruits.items():
        # print(key,value)
        heapq.heappush(q, (-value, key)) # 개수가 가장 많은 귤부터 꺼내기 위해서 개수인 value에 - 를 붙여서 heapq에 넣는다

    ## 담은 귤의 수가 k보다 넘지 않는지 기록하기 위한 변수
    cnt = k
    while q:
        now = -heapq.heappop(q)[0] # 현재 귤의 개수를 저장

        # 만약에 담을 수 있는 귤의 수-1 한 값이 0보다 크면, 해당 귤을 가지수에 추가 가능!
        # 추가한 후에 cnt를 현재 귤 개수만큼 줄여주기
        if cnt - 1 >= 0:
            answer += 1
            cnt -= now

        # 담을 수 있는 개수 k 보다 귤을 많이 담았다면 while 종료
        else:
            break

    return answer

## set key,value 쌍 출력하기
# set.items()