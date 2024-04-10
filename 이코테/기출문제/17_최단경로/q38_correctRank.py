## 기출문제 - 최단경로 38.정확한 순위
# 성적 순위를 정확히 알 수 없는 학생 수 구하기
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n : 학생 수, m : 성적 비교 횟수

score = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    score[a].append(b)
answer = [0]*(n+1)

def find(a):
    for i in score[a]:
        for j in score[i]:
            if j not in score[a]:
                score[a].append(j)

for i in range(1,n+1):
    find(i)

for i in range(1, n+1):
    answer[i] += len(score[i])
    for j in score[i]:
        answer[j] += 1

result = 0
for i in range(1, n+1):
    if answer[i] == n-1:
        result += 1


print(result)

## input
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

## 문제 풀이
# 플로이드워셜을 써야 하는데, 걍 무분별하게 for문을 많이 돌려서 해결했다
# 사실 테스트케이스가 1개라서 이걸 해결했다고 해도 되는건가 싶다!
# 어딘가 시간초과 혹은 메모리초과가 날 것만 같다..