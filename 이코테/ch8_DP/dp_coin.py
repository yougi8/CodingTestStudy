import sys
## 잘 이해가 안갑니다 ㅠㅠ
n,m = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [10001] * (m+1) # m까지의 화폐가 필요한 개수?를 저장하는 배열
dp[0] = 0 # 0원은 화폐 0개를 가지고 만들 수 있으니까 0

# 주어진 화페를 돌면서 몇개가 필요한지를 파악할거야 (ex. 2,3,5)
for i in range(n):
    for j in range(arr[i], m+1): # 해당 화폐부터 화폐 최대단위까지 살펴보기(ex. 2~7 / 3~7 / 5~7)
        dp[j] = min(dp[j], dp[j-arr[i]]+1) # 더 작은 값으로 교체해주기

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
