## 기출문제 - 이진탐색 q28. 고정점 찾기
# 고정점 : 그 값이 인덱스와 동일한 원소

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = -1

def find(start,end):
    global answer
    mid = (start+end)//2
    if start>end:
        return
    if mid == arr[mid]:
        answer = mid
        return
    elif arr[mid]>mid:
        find(start,mid-1)
    else:
        # find(start, mid-1)
        find(mid+1, end)

find(0,n-1)
print(answer)

## input - output
# 5
# -15 -6 1 3 7 => 3
# 7
# -15 -4 2 8 9 13 15 => 2
# 7
# -15 -4 3 8 9 13 15 => -1

## 문제 풀이
# arr[mid]값이 mid값과 같다면 해당 값 출력
# arr[mid]값이 mid값보다 크다면, 왼쪽탐색
# arr[mid]값이 mid값보다 작다면, 오른쪽 탐색

