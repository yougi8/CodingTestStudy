## 이코테 기출문제 정렬 - 24. 안테나(Sw마에스트로 입학 테스트/ 백준 18310)
# 안테나를 설치할 위치의 값 출력 (여러개면 가장 작은 값)

import sys
input = sys.stdin.readline
n = int(input()) # 집의 수 n 1이상 200000 이하
arr = list(map(int, input().split())) # 집의 위치 1이상 100000 이하

arr.sort()

print(arr[(n-1)//2])

## 문제풀이
# 집 배열을 sort해서 중간값을 선택하면 된다.