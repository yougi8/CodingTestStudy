## 7-3 반복문으로 구현한 이진 탐색
import sys
def binary_search(start,end,target,array):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None
n, target = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

result = binary_search(0, n-1, target, array)
if result == None:
    print('찾으려는 원소가 없습니다.')
else:
    print(result+1)