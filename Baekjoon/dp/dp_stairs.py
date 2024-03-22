## 백준 dp silver3 2579 계단 오르기
import sys
n = int(sys.stdin.readline()) # n개의 계단

arr = [] # 계단의 점수가 입력되는 배열

for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0] * n # 점화식 기록할 배열

## 계단이 2개 이하이면, 다 더하기
if n<=2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i]) ## 연속해서 온거지, 두칸 뛰어서 온건지 두가지 경우를 비교해서 선택
    print(dp[n-1])