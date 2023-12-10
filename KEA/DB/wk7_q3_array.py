# [이코테] 이진탐색 - 정렬된 배열에서 특정 수의 개수 구하기
import sys
def count_func(arr, target):
    n = len(arr)

    idx1 = first(arr, target, 0, n-1) # target값 가지고 있는 시작 index

    if idx1 == None:
        return 0
    
    idx2 = last(arr, target, 0, n-1) # target값 가지고 있는 마지막 index

    return idx2-idx1+1

def first(arr,target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # mid값이 0이고(맨 왼쪽값), 중간값이 target값과 같으면 맨 왼쪽 index 찾은거임!
    # 혹은, target값이 중간값-1 값보다 크고(찾고자 하는 값 중에서 가장 왼쪽인 놈을 찾은것), 중간값이 target값과 같으면 찾은것!
    if ( mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target: # 왼쪽 탐색
        return first(arr, target, start, mid-1)
    else:
        return first(arr, target, mid+1, end) # 오른쪽 탐색

def last(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # mid값이 가장 오른쪽 값이고, 중간값이 target값과 같으면 맨 오른쪽 index 찾은거임!
    # 혹은, target값이 중간값+1 값보다 작고(그니까 찾고자 하는 값 중에서 가장 오른쪽인 놈을 만난거임), 중간값이 target값과 같으면 찾은거임!
    if ( mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    # 지금은 가장 오른쪽에 있는 index를 찾는 것이기 때문에 >= 가 아닌, > 일 경우만 비교하면 된다. 
    # 만약 222 중에서 가운데 2에 걸렸는데 왼쪽을 탐색하게 되면 마지막 index를 찾을 기회를 날린거다!
    elif arr[mid] > target:
        return last(arr, target, start, mid-1) # 왼쪽 탐색
    else:
        return last(arr, target, mid+1, end) # 오른쪽 탐색
    

n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = count_func(arr,x)

if result == 0 :
    print(-1)
else:
    print(result)