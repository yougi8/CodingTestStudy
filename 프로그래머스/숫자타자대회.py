## 프로그래머스 - 숫자 타자 대회 https://school.programmers.co.kr/learn/courses/30/lessons/136797
from collections import defaultdict
import sys
import math

sys.setrecursionlimit(200000)
# cache[i][(left, right)]
# i번째 숫자를 누른 상태에서
# 왼손이 left, 오른손이 right에 있는 경우의 최소 가중치
cache = defaultdict(dict)

# W[i][j]는 i번째 숫자에서 j번째 숫자로 이동하여 누를 때의 가중치 행렬입니다.
W = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],  # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],  # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],  # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],  # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],  # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],  # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],  # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],  # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],  # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],  # 9
]


def solve(i, left, right, numbers):
    if i == len(numbers):
        return 0

    if (left, right) in cache[i]:
        return cache[i][(left, right)]

    w = math.inf
    num = numbers[i]
    # 왼손을 이동하는 경우
    if num != right:
        w = min(w, solve(i + 1, num, right, numbers) + W[left][num])
    # 오른손을 이동하는 경우
    if num != left:
        w = min(w, solve(i + 1, left, num, numbers) + W[right][num])

    cache[i][(left, right)] = w
    return w


def solution(numbers):
    numbers = list(int(x) for x in numbers)
    return solve(0, 4, 6, numbers)

## 문제 해설
# 못 풀었다.
# DP + 재귀 혹은 DP+BFS