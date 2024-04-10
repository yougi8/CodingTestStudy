## 기출문제 - DP q.32 정수 삼각형 (백준 1932)
# 다음 배열의 index가 같거나 1 큰 것만 선택할 수 있다
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
        arr.append(list(map(int, input().split())))

arr[0][0] = arr[0][0]
if n>=2:
    arr[1][0] = arr[0][0]+arr[1][0]
    arr[1][1] = arr[0][0]+arr[1][1]

    for i in range(2, n):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i-1][0]
            elif j == len(arr[i])-1:
                arr[i][j] += arr[i-1][len(arr[i-1])-1]
            else:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))

## input
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

## 문제 풀이
# dp 배열을 따로 선언할 필요 없다 (개선완료)
# dp문제는 n=1일경우를 생각해서 메모리할당 이슈를 반드시반드시 생각해야한다.
# 생각했는데도 그거 때문에 3번 실패함..ㅠㅠ

# 개선전&런타임에러 코드
## 런타임 에러 코드
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for i in range(n):
#         arr.append(list(map(int, input().split())))
#
# dp = [[0]*(n+1) for _ in range(n+1)]
#
# dp[0][0] = arr[0][0]
# dp[1][0] = arr[0][0]+arr[1][0]
# dp[1][1] = arr[0][0]+arr[1][1]
#
# for i in range(2, n):
#     for j in range(len(arr[i])):
#         if j==0:
#             dp[i][j] = dp[i-1][j]+arr[i][j]
#         elif j==len(arr[i])-1:
#             dp[i][j] = dp[i-1][len(arr[i])-2] + arr[i][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-1]+arr[i][j], dp[i-1][j]+arr[i][j])
#
# print(max(dp[n-1]))