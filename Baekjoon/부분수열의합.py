## 백준 실버2 부분수열의 합
import sys
from itertools import combinations
input = sys.stdin.readline

n,s = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

permu = []
for i in range(1,n+1):
    permu.append(list(combinations(nums, i)))

# print(permu)

answer = 0
for i in permu:
    for j in i:
        if sum(j) == s:
            # print(j)
            answer += 1
print(answer)

## input
# 5 0
# -7 -3 -2 5 8
## output
# 1
