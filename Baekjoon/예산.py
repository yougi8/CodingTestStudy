## 백준 실버2 예산 https://www.acmicpc.net/problem/2512
import sys
input = sys.stdin.readline

n = int(input())

requires = list(map(int, input().split()))
requires.sort()

budget = int(input())

answer = 0

if sum(requires) <= budget:
    print(requires[-1])
    exit(0)
else:
    start = 0
    end = requires[-1]

    while start <= end:
        mid = (start+end)//2

        total = 0
        for require in requires:
            if require <= mid:
                total += require
            else:
                total += mid
        if total <= budget:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)



## input 1
# 4
# 120 110 140 150
# 485
## output 1
# 127

## input 2
# 5
# 70 80 30 40 100
# 450
## output 2
# 100