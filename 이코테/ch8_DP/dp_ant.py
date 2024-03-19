import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

## 다이나믹 프로그래밍 : 큰 문제를 작은 문제로 푸는 것!!!

dp = [0]*n ## 약탈 가능한 총 식량의 개수 저장 (앞에서 계산된 결과 저장)

dp[0] = arr[0] # 첫번째 창고는 그냥 첫 번째 값이다.
dp[1] = max(arr[0], arr[1]) # 두 번째 창고는, 첫 번째 창고와 두 번째 창고 중 더 큰 값이 된다.

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+arr[i]) # 현재 위치를 선택 안 하고 그 전을 선택하거나 // 현재 위치 + 전전위치 선택하거나

print(dp[n-1])