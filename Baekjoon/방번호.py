## 백준 방번호 골드3 https://www.acmicpc.net/problem/1082
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
dp = [-1e9]*(m+1)

for i in range(n-1,-1,-1):
    price = numbers[i]

    # 현재 내가 살 수 있는 가격인 price부터 dp를 확인한다. 그 밑은 어차피 해당 숫자를 살 수 없다
    for j in range(price,m+1):
        dp[j] = max(dp[j],dp[j-price]*10+i,i) # 현재 dp값, 이 숫자를 뒤에 붙인 값, 현재 숫자만 가져가는 값 이 셋 중에서 가장 큰 값 선택

print(dp[m])

## 문제 풀이
# 어떤 것을 dp배열로 잡을 지 잘 생각해보자!


## input1
# 3
# 6 7 8
# 21
## output1
# 210
## input2
# 3
# 5 23 24
# 30
## output2
# 20
## input3
# 4
# 1 5 3 2
# 1
## output3
# 0
## input4
# 10
# 1 1 1 1 1 1 1 1 1 1
# 50
## output4
# 99999999999999999999999999999999999999999999999999