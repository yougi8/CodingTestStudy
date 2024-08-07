## 백준 - 타노스 https://www.acmicpc.net/problem/20310
import sys
input = sys.stdin.readline
str = input().strip()

length = len(str)
## 1, 0 개수 구하기
zero = 0
one = 0
for i in range(length):
    if str[i]=='1':
        one += 1
    else:
        zero += 1

cnt_zero = 0
cnt_one = 0
delete = []
# 앞에부터 1 지우기
for i in range(length):
    if cnt_one==one//2:
        break
    if str[i]=='1':
        delete.append(i)
        cnt_one += 1
# 뒤에부터 0 지우기
for i in range(length-1,-1,-1):
    if cnt_zero==zero//2:
        break
    if str[i]=='0':
        delete.append(i)
        cnt_zero += 1

delete.sort()
answer = []
for i in range(length):
    if i not in delete:
        answer.append(str[i])
print(''.join(answer))

# 예제 입력 1
# 1010
# 예제 출력 1
# 01
# 예제 입력 2
# 000011
# 예제 출력 2
# 001

# 제한조건
# S의 길이는 2 이상 500 이하이다.
# S는 짝수 개의 0과 짝수 개의 1로 이루어져 있다.