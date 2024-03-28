## 재귀 함수로 구현한 이진 탐색 소스코드
import sys
def binary_search(start, end, target, array):
    if start > end:
        return None
    else:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target: # 현재 값이 찾는 값보다 크면, 오른쪽에 있으면 -> 왼쪽부분 탐색 == end를 옮겨오기
            return binary_search(start, mid-1, target, array)
        else:
            return binary_search(mid+1, end, target, array)


n, target = list(map(int,sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))
result = binary_search(0, n-1, target, array)
if result == None:
    print("찾으려는 원소가 존재하지 않습니다.")
else:
    print(result+1) # 인덱스 값이 아닌, 몇 번째에 있는지 반환하는 것이기 때문에 +1
