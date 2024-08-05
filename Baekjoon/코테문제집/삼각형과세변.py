## 백준 - 삼각형과 세 변 https://www.acmicpc.net/problem/5073
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split(' ')))
    if arr[0]==0 and arr[1]==0 and arr[2]==0: break

    arr.sort()
    if arr[2] >= arr[0]+arr[1]:
        print('Invalid')
    elif arr[0]==arr[1]==arr[2]:
        print('Equilateral')
    elif arr[0]==arr[1] or arr[1]==arr[2]:
        print('Isosceles')
    else:
        print('Scalene')

## 예제 입력
# 7 7 7
# 6 5 4
# 3 2 5
# 6 2 6
# 0 0 0
## 예제 출력
# Equilateral
# Scalene
# Invalid
# Isosceles