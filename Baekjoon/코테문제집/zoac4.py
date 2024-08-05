## 백준 - zoac4 https://www.acmicpc.net/problem/23971
import sys
import math
input = sys.stdin.readline

h,w,n,m = map(int,input().split(' '))

answer = 0
height = math.ceil(h/(n+1))
width = math.ceil(w/(m+1))

answer = height*width

print(answer)
## 예제 입력
# 5 4 1 1
## 예제 출력
# 6