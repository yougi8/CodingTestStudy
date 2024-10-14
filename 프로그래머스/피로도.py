## 프로그래머스 - 피로도 Lv2. https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations

def solution(k, dungeons):
    permu = list(permutations(dungeons))
    answer_list = []

    for dungeon in permu:
        now = k
        answer = 0
        for need, use in dungeon:
            if now < need:
                break
            else:
                answer += 1
                now -= use
        answer_list.append(answer)
    return max(answer_list)

## 완전탐색 문제로, 풀이 방법이 여러가지가 있다. 이 문제는 경우의 수가 8! 정도밖에 안되기 때문에 조합 사용
# 다른 방법으로는 dfs 백트래킹, 브루트포스, 재귀 등이 있다.