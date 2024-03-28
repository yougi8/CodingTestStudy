## 기출문제 - 이진탐색 q27. 정렬된 배열에서 특정 수의 개수 구하기
import sys
n, x = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

## 개수 찾기
def search(target, array):
    a = first(0, len(array)-1, target, array)
    ## 시작점이 없다면, target값이 존재하지 않는 것이므로 None return
    if a==None:
        return None
    ## 시작점이 존재한다면, 끝점도 찾아주기
    b = last(0, len(array)-1, target, array)

    ## 원소 개수 구하기
    return b-a+1

## 시작 인덱스 찾기
def first(start, end, target, array):
    if start > end:
        return None
    mid = (start+end) // 2

    ## 찾은 mid index부터 0 까지 거꾸로 돌면서, target값이랑 똑같은 가장 왼쪽의 index 찾아주기
    if array[mid] == target:
        index = mid
        for i in range(mid, 0, -1):
            if array[i] == target:
                index = i
        return index
    elif array[mid] > target:
        return first(start, mid-1, target, array)
    else:
        return first(mid+1, end, target,array)

## 끝 인덱스 찾기
def last(start, end, target, array):
    if start > end:
        return None
    mid = (start+end) // 2

    ## 찾은 mid index부터 end index까지 1씩 증가하면서, target값이랑 똑같은 가장 오른쪽의 index 찾아주기
    if array[mid] == target:
        index = mid
        for i in range(mid, end):
            if array[i] == target:
                index = i
        return index
    elif array[mid] > target:
        return last(start, mid-1, target, array)
    else:
        return last(mid+1, end, target,array)

result = search(x, array)
if result == None:
    print(-1)
else:
    print(result)
