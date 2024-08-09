## 백준 - 문제집 - 가희와 키워드 https://acmicpc.net/problem/22233
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

keyword = defaultdict(list)
for i in range(n):
    keyword[input().strip()] = 1

answer = len(keyword)
for i in range(m):
    post = list(map(str, input().strip().split(',')))

    for word in post:
        if word in keyword and keyword[word]==1:
            answer -= 1
            keyword[word] -= 1
    print(answer)

## 예제 입력 1
# 5 2
# map
# set
# dijkstra
# floyd
# os
# map,dijkstra
# map,floyd
## 예제 출력 1
# 3
# 2