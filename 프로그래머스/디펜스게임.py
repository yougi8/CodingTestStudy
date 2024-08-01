## 프로그래머스 디펜스 게임
import heapq
def solution(n, k, enemy):
    cnt = 0
    q = []
    for i, value in enumerate(enemy):
        if n<value and k==0: break
        if n-value>=0:
            n -= value
            heapq.heappush(q,-value)
            cnt += 1
        else:
            live = 0
            if len(q)>0:
                live = heapq.heappop(q)
            n -= live
            k -= 1
            cnt += 1
    print(cnt)
    return cnt

# solution(7,3,[4, 2, 4, 5, 3, 3, 1])
# solution(2,4,[3, 3, 3, 3])
# solution(3, 1, [ 3,4 ])
# solution(5, 1, [3, 1, 1, 1, 2, 2, 10])
print(solution(5, 1, [4, 2, 3, 6]))  # Expected output: 4
