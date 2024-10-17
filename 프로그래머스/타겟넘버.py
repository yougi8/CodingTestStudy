## 프로그래머스 - 타겟넘버 (dfs) https://school.programmers.co.kr/learn/courses/30/lessons/43165
def dfs(numbers, target, depth):
    global answer
    if depth == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return

    dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    dfs(numbers, target, depth + 1)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(numbers, target, 0)

    return answer

## 문제 해설
# recursion 지옥에 빠질 수도 있으니까 조심하기!