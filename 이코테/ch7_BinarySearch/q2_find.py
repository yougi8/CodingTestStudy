## chapter 7 이진탐색 - 2번 부품찾기
# input:
# 5
# 8 3 7 9 2
# 3
# 5 7 9
# output:
# no yes yes
import sys
def find(start, end, target, array):
    if start > end:
        return "no"
    mid = (start+end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return find(start, mid-1, target, array)
    else:
        return find(mid+1, end, target, array)

n = int(sys.stdin.readline())
store_array = list(map(int, sys.stdin.readline().split())) # 가게 보유 부품 리스트
m = int(sys.stdin.readline())
cus_array = list(map(int, sys.stdin.readline().split())) # 손님 요청 부품 리스트
store_array.sort()
cus_array.sort()

for i in range(m):
    print(find(0, n-1, cus_array[i],store_array), end=' ')

# 궁금한 점
# - 재귀함수로 구현했다. 예시답안을 보니 재귀함수로 구현하는 방법은 없던데, 문제가 생기는걸까?

