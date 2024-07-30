# 숫자 카드 n개가 리스트로 주어진다.
# 순서대로 n개의 카드를 꺼낼 때 숫자가 0이면 상자에서 가장 작은 값의 숫자 카드를 꺼내고
# 0이 아닌 숫자 카드가 나오면 상자에 넣었을 때,
# 상자안에 남아있는 카드의 숫자를 작은 카드 순서대로 모두 출력하시오.
# 단, 같은 수의 카드는 없다.(2 < n < 1,000)
import heapq
def solution(n):
    box = []
    for i in n:
        if i==0:
            heapq.heappop(box)
        else:
            heapq.heappush(box,i)
    # box.sort()
    # print(box)
    for i in range(len(box)):
        print(heapq.heappop(box), end=' ')

n = [5, 6, 3, 0, 1, 14, 0, 9, 7, 12, 0]# 입력값
solution(n)

# 힙에 자료 입력은, heapq.heappush(a, b)는 'a'에 'b'를 입력
# 힙에서 자료 출력은, heqpq.heappop(a)는 'a'에서 출력(출력된 값은 가장 작은 값)