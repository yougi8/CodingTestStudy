import sys
import heapq
n = int(sys.stdin.readline())
cards = [] # 출력초과 방지 위해 heapq 사용
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline())) # heapq에 데이터 추가

result = 0

while len(cards) != 1:
    # 카드목록에서 가장 작은 값 두개를 뺀다.
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    result += a+b
    heapq.heappush(cards,a+b) # 방금 계산한 카드값을 다시 heapq에 추가하기


print(result)