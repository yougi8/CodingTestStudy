## 백준 - 보석도둑 골드2 https://www.acmicpc.net/problem/1202
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
gold = []
bags = []
for i in range(N):
    m,v = map(int, input().split())
    gold.append((m,v))
for i in range(K):
    bags.append(int(input().strip()))

gold.sort() # 무게 오름차순으로 정렬
bags.sort() # 가벼운 보석이 무게가 많이 나가는 가방에 들어가면, 작은 가방에는 들어갈 보석이 없을 수도 있으니 작은 가방부터 보석을 넣어준다.

q = [] # 가방에 집어넣을 수 있는 보석의 후보들 담는 힙큐
answer = 0
for bag in bags:
    while gold:
        if gold[0][0]<=bag:
            heapq.heappush(q,-gold[0][1])
            heapq.heappop(gold)
        else:
            break
    if q:
        answer += -heapq.heappop(q)
print(answer)

# 문제 풀이
# 각 가방에는 보석을 한개씩만 넣을 수 있다는 점이 포인트!
# 가능한 모든 무게의 보석 중에서 가장 값이 큰 애를 집어 넣으면 된다.
# 단, 가방이 가벼운 순서로 진행.

## 예제 입력 1
# 2 1
# 5 10
# 100 100
# 11
# 예제 출력 1
# 10
