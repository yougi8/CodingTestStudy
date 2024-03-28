## chapter 7 이진탐색 - 3. 떡볶이 떡 만들기
# 입력 예시 :
# 4 6
# 19 15 10 17
# 출력 예시 :
# 15
import sys
def cut(start, end, sum, array):
    result = 0  # 손님이 가져갈 수 있는 떡의 길이
    height = 0 # 절단기의 최대 높이
    while start <= end:
        mid = (start+end) // 2
        for i in range(n):
            if array[i] > mid:
                result += array[i]-mid
        if result >= sum:
            height = mid
            start = mid+1
        else:
            end = mid-1
    return height


n, m = list(map(int, sys.stdin.readline().split())) # 떡의 개수 n, 떡의 길이 m
array = list(map(int, sys.stdin.readline().split())) # 떡의 개별 높이 리스트

array.sort()
print(cut(0, array[n-1],m,array)) # 가지고 있는 떡의 최대 길이를 기준으로 살펴본다.

# 답안 비교
# - 예시답안에서는 따로 def 선언을 하지 않았다. 그 외에는 비슷