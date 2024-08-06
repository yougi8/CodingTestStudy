## 백준 - 벌집 https://www.acmicpc.net/problem/2292
import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
result = 1

while n > cnt:
    cnt += 6*result
    result += 1
print(result)

# 예제 입력 : 13 / 예제 출력 : 3

## 풀이
# n==1, 2<=n<=7, 그 이상
# 이렇게 세가지 경우로 나눠서 진행했는데, 어딘가가 잘 안맞았던건지 계속 틀렸다.
# 결국 경우의 수를 나누지 않고 한번에 했는데 정답!

# 경우의 수 나눈 코드 : 아래
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cnt = 1
# result = 1
#
# if n==1:
#     print(result)
# elif n>=2 and n<=7:
#     print(2)
# else:
#     result = 3
#     cnt = 18
#     while n > cnt:
#         cnt += 6*result
#         result += 1
#     print(result)